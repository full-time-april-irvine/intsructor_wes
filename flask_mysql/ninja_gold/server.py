from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import random
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdf;lkjasdf"

SCHEMA = 'ninja_gold'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    # prevent someone from reaching this page if they aren't logged in
    if 'user_id' not in session:
        return redirect('/users/new')

    # we need user info for the gold
    db = connectToMySQL(SCHEMA)
    query = 'SELECT * FROM users WHERE id=%(user_id)s;'
    data = {
        'user_id': session['user_id']
    }
    users = db.query_db(query, data)
    user = users[0]

    # we need all locations information
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM locations;"
    locations = db.query_db(query)

    # we need all activities information
    db = connectToMySQL(SCHEMA)
    query = "SELECT activities.gold, activities.created_at, locations.name AS location_name FROM activities JOIN locations ON activities.location_id = locations.id WHERE activities.user_id = %(user_id)s ORDER BY created_at DESC;"
    data = {
        'user_id': session['user_id']
    }
    activities = db.query_db(query, data)
    return render_template('index.html',
                            user = user,
                            locations = locations,
                            activities = activities)

@app.route('/users/new')
def users_new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def users_create():
    errors = []

    if len(request.form['first_name']) < 1:
        errors.append("First name must be at least 1 character")

    if len(request.form['last_name']) < 1:
        errors.append("Last name must be at least 1 character")

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Email address must be valid")

    db = connectToMySQL(SCHEMA)
    query = 'SELECT * FROM users WHERE email=%(email_from_form)s;'
    data = {
        "email_from_form": request.form['email']
    }
    matching_users = db.query_db(query, data)
    if matching_users:
        errors.append("Email already in use")

    if len(request.form['password']) < 8:
        errors.append("Password must be at least 8 characters long")

    if errors:
        for error in errors:
            flash(error)
        return redirect('/users/new')

    print("INFO IS VALID")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    db = connectToMySQL(SCHEMA)
    query = 'INSERT INTO users (first_name, last_name, email, pw_hash) VALUES(%(first_name_from_form)s, %(last_name_from_form)s, %(email_from_form)s, %(hashed_password)s);'
    data = {
        "first_name_from_form": request.form['first_name'],
        "last_name_from_form": request.form['last_name'],
        "email_from_form": request.form['email'],
        "hashed_password": pw_hash,
    }
    user_id = db.query_db(query, data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def users_login():
    db = connectToMySQL(SCHEMA)
    query = 'SELECT * FROM users WHERE email=%(email_from_form)s;'
    data = {
        'email_from_form': request.form['email']
    }
    matching_users = db.query_db(query, data)

    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
            session['user_id'] = user['id']
            return redirect('/')
    flash("Email or password invalid")
    return redirect('/users/new')

@app.route('/process_money', methods=['POST'])
def process_money():
    # create random gold amount between range
    db = connectToMySQL(SCHEMA)
    query = "SELECT min_gold, max_gold FROM locations WHERE id=%(location_id)s;"
    data = {
        'location_id': request.form['location']
    }
    location_list = db.query_db(query, data)
    location = location_list[0]

    curr_gold = random.randint(location['min_gold'], location['max_gold'])

    # update user gold
    db = connectToMySQL(SCHEMA)
    query = "UPDATE users SET gold = gold + %(new_gold)s WHERE id=%(user_id)s;"
    data = {
        'new_gold': curr_gold,
        'user_id': session['user_id']
    }
    db.query_db(query, data)

    # create activity
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO activities (location_id, user_id, gold) VALUES(%(location_id)s, %(user_id)s, %(new_gold)s);"
    data = {
        'location_id': request.form['location'],
        'new_gold': curr_gold,
        'user_id': session['user_id']
    }
    db.query_db(query, data)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/users/new')

if __name__ == "__main__":
    app.run(debug=True)