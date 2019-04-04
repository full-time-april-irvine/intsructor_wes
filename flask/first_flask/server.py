from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    users = ["Wes", "Nina", "Gabe", "Kent", "Cameron"]
    return render_template('index.html', title="thing", users=users)

@app.route('/new/<user_stuff>/edit')
def new(user_stuff):
    return f"This is a cool thing: {user_stuff}"

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)