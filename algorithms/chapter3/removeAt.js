function removeAt(arr, idx) {
  var temp = arr[idx];
  for(var i = idx; i < arr.length; i++) {
    arr[i] = arr[i + 1];
  }
  arr.length--;
  return temp;
}

var testArr = [1, 2, 3, 4];
console.log(removeAt(testArr, 3));
console.log(testArr);