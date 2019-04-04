from flask import Flask, render_template
# from utils import create_checkerboard

app = Flask(__name__)

def create_checkerboard(rows=5, cols=5, color1="red", color2="black"):
    checkerboard = []
    for curr_row in range(rows):
        new_row = []
        for curr_col in range(cols):
            if curr_row % 2 == 0:
                if curr_col % 2 == 0:
                    new_row.append(color1)
                else:
                    new_row.append(color2)
            else:
                if curr_col % 2 == 0:
                    new_row.append(color2)
                else:
                    new_row.append(color1)
        checkerboard.append(new_row)
    return checkerboard

@app.route('/')
def index():
    return render_template(
        'dynamic.html',
        checkerboard = create_checkerboard()
    )

@app.route('/<x>')
def rows(x):
    return render_template(
        'dynamic.html',
        checkerboard=create_checkerboard(int(x))
    )

@app.route('/<x>/<y>')
def rows_cols(x, y):
    return render_template(
        'dynamic.html',
        checkerboard=create_checkerboard(int(x), int(y))
    )

@app.route('/<x>/<y>/<color1>/<color2>')
def all(x, y, color1, color2):
    return render_template(
        'dynamic.html',
        checkerboard=create_checkerboard(int(x), int(y), color1, color2)
    )

if __name__ == "__main__":
    app.run(debug=True)