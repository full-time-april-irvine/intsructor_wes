from flask import Flask, render_template, Response, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    errors = {}
    if len(request.form['first_name']) < 2:
        errors['first_name'] = "first name must be at least 2 characters"
    if len(request.form['last_name']) < 2:
        errors['last_name'] = "last name must be at least 2 characters"
    if len(request.form['email']) < 2:
        errors['email'] = "email must be at least 2 characters"
    if len(request.form['password']) < 8:
        errors['password'] = "password must be at least 8 characters"

    if errors:
        return Response(json.dumps(errors), status=400, mimetype="application/json")
    else:
        successful_dictionary = {
            "message": "You did it!"
        }
        return Response(json.dumps(successful_dictionary), status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True)