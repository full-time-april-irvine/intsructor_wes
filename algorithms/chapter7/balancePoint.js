function balancePoint(arr) {
  let start = 0;
  let end = arr.length - 1;
  let leftSum = 0;
  let rightSum = 0;
  while(start <= end) {
    if(leftSum < rightSum) {
      leftSum += arr[start];
      start++;
    } else {
      rightSum += arr[end];
      end--;
    }
  }
  return leftSum === rightSum;
}

const test1 = [1, 2, 3, 4, 5, 5];
const test2 = [1, 2, 3, 4, 10];
const test3 = [1, 2, 4, 2, 1];

console.log(balancePoint(test1));
console.log(balancePoint(test2));
console.log(balancePoint(test3));