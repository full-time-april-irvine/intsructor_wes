function pushFront(arr, val) {
  for(var i = arr.length; i > 0; i--) {
    arr[i] = arr[i - 1];
  }
  arr[0] = val;
  return arr;
}

var testArr = [2, 3, 4];
console.log(pushFront(testArr, 1));