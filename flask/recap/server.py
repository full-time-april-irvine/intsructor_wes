from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/other/<user_id>')
def other(user_id):
    print(user_id)
    return render_template('other.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)