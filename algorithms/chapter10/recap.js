// Important things about strings

// Defined using single or double quotes
let stringOne = 'Hello World';
let stringTwo = "Hello again";

// Have indices
console.log(stringOne[1]);

// Immutable
stringOne[2] = 'a';
console.log(stringOne);

// Concatenation
let stringThree = "H" + "a" +"llo World";
console.log(stringThree);

// Regex
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
const REGEX_PATTERN = new RegExp(/[a-zA-Z]\w+/g)
console.log(REGEX_PATTERN.test(stringOne));
console.log(stringOne.match(REGEX_PATTERN));

// ASCII
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt
console.log(stringOne.charCodeAt(3));