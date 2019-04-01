function insertAt(arr, idx, val) {
  for(var i = arr.length; i > idx; i--) {
    arr[i] = arr[i - 1];
  }
  arr[idx] = val;
  return arr;
}

var testArr = [2, 3, 4];
console.log(insertAt(testArr, 3, 1));