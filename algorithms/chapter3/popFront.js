function popFront(arr) {
  var temp = arr[0];
  for(var i = 0; i < arr.length; i++) {
    arr[i] = arr[i + 1];
  }
  arr.length--;
  return temp;
}

var testArr = [1, 2, 3, 4];
console.log(popFront(testArr));
console.log(testArr);