// Climbing Stairs

// Speros walks the stairs at the Dojo multiple times every day.Often he takes 2 stairs at a time, to work his quadriceps; he’s just that way.Other days he mixes it up: with every footstep, he randomly chooses to take 1 stair or 2. You are given an integer representing the total number of stairs.Determine all ways to walk the stairs.Given 4, return [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]].Solve recursively with no loops.And don’t forget to get yourself some exercise during the bootcamp, as well.

//   Second: assuming you always start with a left foot, return only those ways that end with a right step.So, given 4, you should return [[1, 1, 1, 1], [2, 2]].

//     Third: instead of only returning those that end with a right step, only return those where the total number of steps climbed with left foot equal those climbed with right.So, given 4, you should return [[1, 1, 1, 1], [1, 2, 1], [2, 2]].

function climbingStairs(numStairs, options = {}) {
  const result = [];
  function recurse(currentSequence=[], currentSum=0) {
    if(currentSum === numStairs) {
      result.push(currentSequence);
    } else if(currentSum < numStairs) {
      recurse([...currentSequence, 1], currentSum + 1);
      recurse([...currentSequence, 2], currentSum + 2);
    }
    return;
  }
  recurse();

  // parts 2 and 3
  if(options.endWithRight) {
    return result.filter((arr) => {
      return arr.length % 2 === 0;
    });
  } else if(options.leftRightEqual) {
    return result.filter((arr) => {
      let leftFootSum = 0;
      let rightFootSum = 0;
      for(let i = 0; i < arr.length; i++) {
        if(i % 2 === 0) {
          leftFootSum += arr[i];
        } else {
          rightFootSum += arr[i];
        }
      }
      return leftFootSum === rightFootSum;
    });
  }
  return result;
}

console.log(climbingStairs(4));
console.log(climbingStairs(4, {endWithRight: true})); // part 2
console.log(climbingStairs(4, {leftRightEqual: true})); // part 3