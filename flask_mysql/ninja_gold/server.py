from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
import random

SCHEMA = 'ninja_gold_no_login'
app = Flask(__name__)

@app.route('/')
def index():
    # we need user info for the gold
    db = connectToMySQL(SCHEMA)
    query = 'SELECT * FROM users WHERE id=1;'
    users = db.query_db(query)
    user = users[0]

    # we need all locations information
    db = connectToMySQL(SCHEMA)
    query = "SELECT * FROM locations;"
    locations = db.query_db(query)

    # we need all activities information
    db = connectToMySQL(SCHEMA)
    query = "SELECT activities.gold, activities.created_at, locations.name AS location_name FROM activities JOIN locations ON activities.location_id = locations.id ORDER BY created_at DESC;"
    activities = db.query_db(query)
    return render_template('index.html',
                            user = user,
                            locations = locations,
                            activities = activities)

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
    query = "UPDATE users SET gold = gold + %(new_gold)s WHERE id=1;"
    data = {
        'new_gold': curr_gold
    }
    db.query_db(query, data)

    # create activity
    db = connectToMySQL(SCHEMA)
    query = "INSERT INTO activities (location_id, user_id, gold) VALUES(%(location_id)s, 1, %(new_gold)s);"
    data = {
        'location_id': request.form['location'],
        'new_gold': curr_gold
    }
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)