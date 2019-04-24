from flask import Flask, render_template, Response
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partial')
def partial():
    users_list = ['Wes', 'JK', 'Dzung', 'Cameron', "Kent", "Nina", "Keevin", "Addicus"]
    return render_template('partial.html', users=users_list)

@app.route('/json')
def api():
    json_data = json.dumps({
        "favorite_food": "sushi",
        "favorite_color": "mint green"
    })
    return Response(response=json_data, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)