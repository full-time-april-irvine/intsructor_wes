from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "asdfasdfj;laksf;"

@app.route('/')
def index():
    # This will render the login and registration page
    # return render_template("login_reg.html")
    pass

@app.route('/books')
def books_index():
    # This will render a page with all books on it
    # Will have a SELECT query for all books
    # Will render books_index.html
    pass

@app.route('/books/<id>')
def books_show(id):
    pass

@app.route('/add_like/<book_id>')
def add_like_to_book(book_id):
    pass

@app.route("/authors")
def authors_index():
    pass

@app.route('/authors/<id>')
def authors_show(id):
    pass

if __name__ == "__main__":
    app.run(debug=True)