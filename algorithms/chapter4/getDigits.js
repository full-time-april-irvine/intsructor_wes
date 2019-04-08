var testStr = "0s1a3y5w7h9a2t4?6!8?0";

function getDigits(str) {
  var result = "";
  for(var i = 0; i < str.length; i++) {
    for(var j = 0; j < 10; j++) {
      if (str[i] == j) {
        result += str[i];
      }
    }
  }
  // console.log(result);
  return parseInt(result);
}

function getDigits2(str) {
  var result = "";
  for(var i = 0; i < str.length; i++) {
    if(str[i].match(/[0-9]+/)) {
      result += str[i];
    }
  }
  // console.log(result);
  return parseInt(result);
}

console.log(getDigits2(testStr));

// console.log(parseInt("h") === NaN);