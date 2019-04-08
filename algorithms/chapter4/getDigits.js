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

function getDigits3(str) {
  // associate each string with its digit value
  var numberMap = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9 }
  // digitPlace represents "ones", "tens", "hundreds", etc. 
  // in other words, where should the digit go?
  var digitPlace = 1;
  var resultNum = 0;
  // loop through the input string backward
  for (var i = str.length - 1; i >= 0; i--) {
    // use the quick lookup speed of the object to check for the existence of a key
    if(numberMap[str[i]] !== undefined) {
      // if key exists, add to result in the proper "place"
      resultNum += numberMap[str[i]] * digitPlace;
      digitPlace *= 10;
    }
  }
  return resultNum;
}
console.log(getDigits3("0s1a3y5w7h9a2t4?6!8?0"))

// console.log(parseInt("h") === NaN);