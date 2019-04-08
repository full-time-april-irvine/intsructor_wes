from flask import Flask, redirect, request, render_template, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "asdflkjads;fjkasdf"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    
    if 'activities' not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    building_map = {
        'farm': random.randint(10,20),
        'cave': random.randint(5,10),
        'house': random.randint(2,5),
        'casino': random.randint(-50,50),
    }
    
    building = request.form['building']
    curr_gold = building_map[building]

    session['gold'] += curr_gold

    now = datetime.now().strftime('%Y/%m/%d %I:%M %p')

    if curr_gold > 0:
        activity = {
            'content': f"Earned {curr_gold} golds from the {building}! ({now})",
            'css_class': 'green-text'
        }
    else:
        activity = {
            'content': f"Entered the {building} and lost {curr_gold} golds... Ouch. ({now})",
            'css_class': 'red-text'
        }
    
    session['activities'].insert(0, activity)
    print(session['activities'])

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)