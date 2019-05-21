var arr = [1, 1, 1, 1, 1, 1, 1, 1];

if(arr[1] instanceof Array) {
  console.log('it is an array!');
} else {
  console.log("it isn't an array");
}

for(var i = 0; i < arr.length; i++) {
  console.log(i);
  arr.pop();
}