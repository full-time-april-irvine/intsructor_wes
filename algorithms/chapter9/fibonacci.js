// Create a function to generate Fibonacci numbers.In this famous mathematical sequence, each number is the sum of the previous two, starting with values 0 and 1. Your function should accept one argument, an index into the sequence(where 0 corresponds to the initial value, 4 corresponds to the value four later, etc).Examples: fibonacci(0) = 0(given), fibonacci(1) = 1(given), fibonacci(2) = 1(fib(0) + fib(1), or 0 + 1), fibonacci(3) = 2(fib(1) + fib(2), or 1 + 1), fibonacci(4) = 3(1 + 2), fibonacci(5) = 5(2 + 3), fibonacci(6) = 8(3 + 5), fibonacci(7) = 13(5 + 8), etc.

// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

// function fibonacci(idx) {
//   var a = 0;
//   var b = 1;
//   for(var i = 0; i < idx; i++) {
//     var temp = a + b;
//     a = b;
//     b = temp;
//   }
//   return a;
// }

// console.log(fibonacci(6));

function fibonacci(idx, a=0, b=1) {
  if(idx <= 0) {
    return a;
  }
  return fibonacci(idx - 1, b, a + b);
}

console.log(fibonacci(6));