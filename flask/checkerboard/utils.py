def create_checkerboard(rows=5, cols=5, color1="red", color2="black"):
    return [[((color1, color2), (color2, color1))[curr_row % 2][curr_col % 2] for curr_col in range(cols)] for curr_row in range(rows)]

print(create_checkerboard())