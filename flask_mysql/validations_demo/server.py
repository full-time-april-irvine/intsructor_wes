from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
app.secret_key = 'asdf;alskjdf;lakjsdf'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    db = connectToMySQL('pets')
    pets = db.query_db("SELECT * FROM pets")
    return render_template('index.html', all_pets = pets)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/process', methods=['POST'])
def process():
    valid = True
    # name can't be blank
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
        valid = False
    # type can't be blank
    if len(request.form['type']) < 1:
        flash("Type cannot be blank")
        valid = False
    # age must be an integer
    # try to do something that we expect to cause an error
    try:
        int(request.form['age'])
    # if there is an error in the "try" block, run the except block
    except ValueError:
        flash("Age must be an integer")
        valid = False
    # email address must be in a valid format
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email must be valid")
        valid = False
    # email address must be unique
    db = connectToMySQL('pets')
    query = "SELECT * FROM pets WHERE email=%(em)s;"
    data = {
        "em": request.form['email']
    }
    matching_pets_list = db.query_db(query, data)
    # a SELECT query will always return a list
    # we can use whether or not the list was empty to infer uniqueness
    # if list is not empty, at least one email in db must have matched
    if len(matching_pets_list) > 0:
        flash("Email already in use")
        valid = False

    if not valid:
        return redirect('/new')
    else:
        # create a pet
        db = connectToMySQL('pets')
        query = 'INSERT INTO pets (name, type, age, email) VALUES (%(n)s, %(t)s, %(a)s, %(e)s);'
        data = {
            'e': request.form['email'],
            'n': request.form['name'],
            'a': request.form['age'],
            't': request.form['type'],
        }
        db.query_db(query, data)
    return redirect('/')

@app.route('/click_on_specific_pet_form', methods=['POST'])
def click():
    print("*" * 80)
    print(request.form)
    print("*" * 80)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)