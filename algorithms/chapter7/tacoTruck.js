function tacoTruck(coords) {
  xMed = coords.sort((a, b) => a[0] - b[0])[Math.trunc(coords.length / 2)][0];
  yMed = coords.sort((a, b) => a[1] - b[1])[Math.trunc(coords.length / 2)][1];
  return [xMed, yMed];
}