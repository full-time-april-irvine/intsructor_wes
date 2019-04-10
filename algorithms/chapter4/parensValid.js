function parensValid(str) {
  var opens = [];
  for(var i = 0; i < str.length; i++) {
    if (str[i] === "(") {
      opens.push(str[i])
    } else if (str[i] === ")") {
      if (opens.length === 0) return false;
      opens.pop()
    }
  }
  return opens.length === 0;
}

console.log(parensValid("(()"));
console.log(parensValid("(()))"));
console.log(parensValid("(())"));