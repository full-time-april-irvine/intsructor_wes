function bracesValid(str) {
  var bracesMap = {
    "}": "{",
    "]": "[",
    ")": "(",
  };
  var bracesStack = [];
  for(var i = 0; i < str.length; i++) {
    if(str[i] === "(" || str[i] === '[' || str[i] === "{") {
      bracesStack.push(str[i]);
    } else if (str[i] === ")" || str[i] === ']' || str[i] === "}") {
      if(bracesMap[str[i]] !== bracesStack.pop()) {
        return false;
      }
    }
  }
  return bracesStack.length === 0;
}

console.log(bracesValid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"))
console.log(bracesValid("D(i{a}l[ t]o)n{e"))
console.log(bracesValid("A(1)s[O (n]0{t) 0}k"))

var arr = [1, 2, 3]
var last = arr.pop()
console.log(last, arr);