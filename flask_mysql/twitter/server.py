from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re
from filters import time_formatter

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfl;kjasdf;lkj"

app.jinja_env.filters['time_formatter'] = time_formatter

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA_NAME = 'twitter'

@app.route('/')
def index():
    # check to see if someone is logged in
    if 'user_id' not in session:
        return redirect('/users/new')

    db = connectToMySQL(SCHEMA_NAME)
    query = """SELECT users.username, tweets.content, tweets.created_at FROM tweets
            JOIN users ON users.id = tweets.creator_id
            ORDER BY tweets.created_at DESC;"""
    tweet_list = db.query_db(query)
    return render_template('index.html', tweets=tweet_list)

@app.route('/users/new')
def users_new():
    return render_template('login_and_reg.html')

@app.route('/register', methods=['POST'])
def register():
    errors = []

    # username cannot be blank
    if len(request.form['username']) < 1:
        errors.append('Username cannot be left blank')

    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT * FROM users WHERE username=%(un)s;"
    data = {
        "un": request.form['username']
    }
    matching_users = db.query_db(query, data)
    # email must be valid format
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append('Email must be valid')
    # email must be unique
    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT * FROM users WHERE email=%(em)s;"
    data = {
        "em": request.form['email']
    }
    matching_users = db.query_db(query, data)
    if matching_users:
        errors.append("Email already in use")
    # password must be at least 8 characters
    if len(request.form['password']) < 8:
        errors.append('Password must be at least 8 characters long')
    
    if errors:
        for error in errors:
            flash(error)
        return redirect('/users/new')

    # add the user to the db
    # before we can add user, we MUST hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    db = connectToMySQL(SCHEMA_NAME)
    query = 'INSERT INTO users (username, email, pw_hash) VALUES(%(un)s, %(em)s, %(pw)s)'
    data = {
        'un': request.form['username'],
        'em': request.form['email'],
        'pw': pw_hash
    }
    user_id = db.query_db(query, data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT id, pw_hash FROM users WHERE username = %(un)s;"
    data = {
        'un': request.form['username']
    }
    matching_users = db.query_db(query, data)
    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
            session['user_id'] = user['id']
            return redirect('/users/new')

    flash("Username or password invalid")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)