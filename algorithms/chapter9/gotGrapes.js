function gotGrapes(arr, idx = -2, currTotal = 0) {
  var temp1 = 0;
  var temp2 = 0;
  if (idx + 2 < arr.length) {
    temp1 = gotGrapes(arr, idx + 2, currTotal + arr[idx + 2]);
  } else {
    return currTotal;
  }
  if (idx + 3 < arr.length) {
    temp2 = gotGrapes(arr, idx + 3, currTotal + arr[idx + 3]);
  }
  return temp1 > temp2 ? temp1 : temp2;
  // if (temp1 > temp2) {
  //   return temp1;
  // } else {
  //   return temp2;
  // }
}

const test1 = [2, 1, 2, 1, 2, 1, 2]; // 8
const test2 = [1, 2, 1, 2, 1, 2, 1]; // 6
const test3 = [1, 2, 100, 2, 1, 2, 1]; // 103

console.log(gotGrapes(test1));
console.log(gotGrapes(test2));
console.log(gotGrapes(test3));