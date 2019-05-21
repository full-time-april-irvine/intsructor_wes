var arr = [
  [3, 2, 3, 4, 3],
  [2, 3, 3, 4, 0],
  [7, 3, 3, 5, 3],
  [6, 5, 3, 4, 1],
  [1, 2, 3, 3, 3]
]

function floodFill(canvas, start, newColor) {
  const x = start[0];
  const y = start[1];
  const color = canvas[y][x];
  canvas[y][x] = newColor;
  if(canvas[y + 1] && canvas[y + 1][x] === color) {
    floodFill(canvas, [x, y + 1], newColor);
  }
  if(canvas[y - 1] && canvas[y - 1][x] === color) {
    floodFill(canvas, [x, y - 1], newColor);
  }
  if(canvas[y][x + 1] !== undefined && canvas[y][x + 1] === color) {
    floodFill(canvas, [x + 1, y], newColor);
  }
  if(canvas[y][x - 1] !== undefined && canvas[y][x - 1] === color) {
    floodFill(canvas, [x - 1, y], newColor);
  }
  return canvas;
}

console.log(floodFill(arr, [2, 2], 0));