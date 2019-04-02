// Sara is looking to hire an awesome web developer and has received applications from various sources.Her assistant alphabetized them but noticed some duplicates.Given a sorted array, remove duplicate values.Because array elements are already in order, all duplicate values will be grouped together.As with all these array challenges, do this without using any built -in array methods.

// Second: solve this without using any nested loops.
var test1 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5];
var test2 = [1, 2, 3, 4, 5];

function removeDuplicates(arr) {
  var newArr = [];
  for(var i = 0; i < arr.length; i++) {
    var isDupe = false;
    for(var j = 0; j < newArr.length; j++) {
      if(arr[i] === newArr[j]) {
        isDupe = true;
        break;
      }
    }
    if(!isDupe) {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

// console.log(removeDuplicates(test1));
// console.log(removeDuplicates(test2));

function removeDuplicates2(arr) {
  var map = {};
  var result = [];
  for(var i = 0; i < arr.length; i++) {
    if(!map[arr[i]]) {
      map[arr[i]] = true;
      result.push(arr[i]);
    }
  }
  return result;
}

// console.log(removeDuplicates2(test1));
// console.log(removeDuplicates2(test2));

function removeDuplicates3(arr) {
  for(var i = 0; i < arr.length - 1; i++) {
    if(arr[i] === arr[i + 1]) {
      for(var j = i + 1; j < arr.length - 1; j++) {
        arr[j] = arr[j + 1];
      }
      arr.length--;
      i--;
    }
  }
  return arr;
}

// console.log(removeDuplicates3(test1));
// console.log(removeDuplicates3(test2));

// Michael + Gabe's solution
function removeduplicate(arr) {
  n_arr = [arr[0]];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i] != n_arr[n_arr.length - 1]) {
      n_arr.push(arr[i]);
    }
  }
  return n_arr
}

// console.log(removeduplicate(['mike', 'mike', 'gabe', 'gabe', 'gabe', 'michael', 'michael', 'michael', 'michael', 'obadian', 'obadian']));