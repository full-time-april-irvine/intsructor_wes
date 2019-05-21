// Given num, return the product of ints from 1 up to num.If less than zero, treat as zero.If not integer, truncate.Experts tell us 0! is 1.rFact(3) = 6(1 * 2 * 3).Also, rFact(6.5) = 720(1 * 2 * 3 * 4 * 5 * 6).

// function rFact(num) {
//   num = Math.trunc(num)
//   var product = 1;

//   function recurse(n) {
//     if(n <= 1) {
//       return product;
//     }
//     product *= n;
//     recurse(n - 1);
//   }

//   return recurse(num);
// }


function rFact(num, product=1) {
  num = Math.trunc(num);
  if(num <= 1) {
    return product;
  }
  return rFact(num - 1, product * num);
}
console.log(rFact(6));