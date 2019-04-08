from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    db = connectToMySQL('world')
    all_cities = db.query_db("SELECT * FROM cities ORDER BY name;")
    return render_template('index.html', cities=all_cities)

@app.route('/process', methods=['POST'])
def process():
    data = {
        'city_name': request.form['city_name']
    }
    query = "INSERT INTO cities (country_code, district, population, country_id, name) VALUES('AUS', 'asdfasdf', 123123, 2, %(city_name)s);"
    db = connectToMySQL('world')
    db.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)