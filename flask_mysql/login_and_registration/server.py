from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfl;kjasdf;lkj"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA_NAME = 'login_and_registration'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/register', methods=['POST'])
def register():
    errors = []

    # first name cannot be blank
    if len(request.form['first_name']) < 1:
        errors.append('First name cannot be left blank')
    # last name cannot be blank
    if len(request.form['last_name']) < 1:
        errors.append('Last name cannot be left blank')
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
        return redirect('/')

    # add the user to the db
    # before we can add user, we MUST hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    db = connectToMySQL(SCHEMA_NAME)
    query = 'INSERT INTO users (first_name, last_name, email, pw_hash) VALUES(%(first)s, %(last)s, %(em)s, %(pw)s)'
    data = {
        'first': request.form['first_name'],
        'last': request.form['last_name'],
        'em': request.form['email'],
        'pw': pw_hash
    }
    user_id = db.query_db(query, data)
    session['user_id'] = user_id
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT id, pw_hash FROM users WHERE email = %(em)s;"
    data = {
        'em': request.form['email']
    }
    matching_users = db.query_db(query, data)
    if matching_users:
        user = matching_users[0]
        if bcrypt.check_password_hash(user['pw_hash'], request.form['password']):
            session['user_id'] = user['id']
            return redirect('/success')

    flash("Email or password invalid")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)