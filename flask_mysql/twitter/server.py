from flask import Flask, render_template, redirect, request, session, flash
# from urlparse import urlparse
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
    query = """SELECT users.id AS creator_id, users.username, tweets.content, tweets.created_at, tweets.id, COUNT(likes.id) AS num_likes FROM tweets
                LEFT JOIN users ON users.id = tweets.creator_id
                LEFT JOIN likes ON tweets.id = likes.tweet_id
                GROUP BY likes.tweet_id, creator_id, users.username, tweets.content, tweets.created_at, tweets.id
                ORDER BY tweets.created_at DESC;"""
    tweet_list = db.query_db(query)

    db = connectToMySQL(SCHEMA_NAME)
    query = """SELECT username FROM users
                WHERE id = %(user_id)s"""
    data = {
        "user_id": session['user_id']
    }
    user_list = db.query_db(query, data)
    specific_user = user_list[0]
    return render_template('index.html', tweets=tweet_list, user=specific_user)

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
            return redirect('/')

    flash("Username or password invalid")
    return redirect('/users/new')

@app.route('/add_like/<tweet_id>')
def add_like(tweet_id):
    print("*" * 80)
    print("user_id:", session['user_id'])
    print("tweet_id:", tweet_id)
    print("*" * 80)
    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT id FROM likes WHERE tweet_id = %(t_id)s AND user_id = %(u_id)s;"
    data = {
        "t_id": tweet_id,
        "u_id": session['user_id']
    }
    matching_likes = db.query_db(query, data)
    if matching_likes:
        return redirect(request.referrer)

    db = connectToMySQL(SCHEMA_NAME)
    query = """INSERT INTO likes (tweet_id, user_id)
                VALUES(%(t_id)s, %(u_id)s);"""
    data = {
        't_id': tweet_id,
        'u_id': session['user_id']
    }
    db.query_db(query, data)
    return redirect(request.referrer)

@app.route('/users/<pizza>/show')
def users_show(pizza):
    print("*" * 80)
    print("Show route, user_id:", pizza)
    print("*" * 80)
    db = connectToMySQL(SCHEMA_NAME)
    query = """SELECT users.username, tweets.content, tweets.created_at, tweets.id, COUNT(likes.id) AS num_likes FROM tweets
                LEFT JOIN users ON users.id = tweets.creator_id
                LEFT JOIN likes ON tweets.id = likes.tweet_id
                WHERE tweets.creator_id = %(u_id)s
                GROUP BY likes.tweet_id, users.username, tweets.content, tweets.created_at, tweets.id
                ORDER BY tweets.created_at DESC;"""
    data = {
        "u_id": pizza
    }
    tweet_list = db.query_db(query, data)

    db = connectToMySQL(SCHEMA_NAME)
    query = """SELECT username FROM users
                WHERE id = %(user_id)s"""
    data = {
        "user_id": pizza
    }
    user_list = db.query_db(query, data)
    specific_user = user_list[0]
    return render_template('users_show.html', tweets=tweet_list, user=specific_user)

@app.route('/tweets/<tweet_id>/delete', methods=["POST"])
def tweets_destroy(tweet_id):
    if 'user_id' not in session:
        return redirect('/users/new')
    
    # check to see that logged in user is creator of current tweet
    db = connectToMySQL(SCHEMA_NAME)
    query = "SELECT creator_id FROM tweets WHERE id=%(t_id)s;"
    data = {
        't_id': tweet_id
    }
    list_of_matching_tweets = db.query_db(query, data)
    specific_tweet = list_of_matching_tweets[0]
    if session['user_id'] != specific_tweet['creator_id']:
        return redirect(request.referrer)

    db = connectToMySQL(SCHEMA_NAME)
    query = "DELETE FROM likes WHERE tweet_id = %(t_id)s;"
    data = {
        "t_id": tweet_id
    }
    db.query_db(query, data)

    db = connectToMySQL(SCHEMA_NAME)
    query = "DELETE FROM tweets WHERE id = %(t_id)s;"
    data = {
        "t_id": tweet_id
    }
    db.query_db(query, data)

    return redirect('/')

@app.route('/tweets/create', methods=['POST'])
def tweets_create():
    errors = []

    if len(request.form['content']) < 1:
        errors.append('Tweet cannot be empty')
    
    if len(request.form['content']) > 255:
        errors.append("Tweet cannot exceed 255 characters")

    if errors:
        for error in errors:
            flash(error)
    else:
        db = connectToMySQL(SCHEMA_NAME)
        query = "INSERT INTO tweets (content, creator_id) VALUES(%(cont)s, %(c_id)s);"
        data = {
            "cont": request.form['content'],
            "c_id": session['user_id'],
        }
        db.query_db(query, data)

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)