function binarySearch(arr, val) {
  if(arr === undefined || val === undefined) {
    return false;
  }

  let leftBound = 0;
  let rightBound = arr.length - 1;
  if(arr[leftBound] === val || arr[rightBound] === val) {
    return true;
  }

  while(leftBound < rightBound - 1) {
    let mid = Math.trunc(((rightBound - leftBound) / 2) + leftBound);
    if(arr[mid] < val) {
      leftBound = mid;
    } else if(arr[mid] > val) {
      rightBound = mid;
    } else {
      return true;
    }
  }
  return false;
}

module.exports = {
  binarySearch,
}