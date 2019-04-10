function intToRoman(num) {
  var denoms = [
    {
      romanNumeral: "M",
      divisor: 1000
    },
    {
      romanNumeral: "D",
      divisor: 500
    },
    {
      romanNumeral: "CD",
      divisor: 400
    },
    {
      romanNumeral: "C",
      divisor: 100
    },
    {
      romanNumeral: "XC",
      divisor: 90
    },
    {
      romanNumeral: "L",
      divisor: 50
    },
    {
      romanNumeral: "XL",
      divisor: 40
    },
    {
      romanNumeral: "X",
      divisor: 10
    },
    {
      romanNumeral: "IX",
      divisor: 9
    },
    {
      romanNumeral: "V",
      divisor: 5
    },
    {
      romanNumeral: "IV",
      divisor: 4
    },
    {
      romanNumeral: "I",
      divisor: 1
    },
  ]
  var romanString = "";
  for (var i = 0; i < denoms.length - 1; i++) {
    var div = denoms[i].divisor;
    var rNum = denoms[i].romanNumeral;
    if(num >= div) {
      romanString += rNum.repeat(Math.trunc(num / div));
      num %= div;
    }
  }
  return romanString;
}
console.log(intToRoman(99));