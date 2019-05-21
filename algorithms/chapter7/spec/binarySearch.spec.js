const binarySearch = require('../binarySearch').binarySearch

describe('`binarySearch()`', function() {
  test('returns true if val is in the given array and the given array has even length', function() {
    expect(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 6)).toBe(true);
  });

  test('returns true if val is in the given array and the given array has odd length', function() {
    expect(binarySearch([1, 2, 3, 4, 5], 2)).toBe(true);
  });

  test('returns true if val is in the given array and the given array has < 2 length', function() {
    expect(binarySearch([4], 4)).toBe(true);
  });

  test('returns true if val is in the given array at the last index', function() {
    console.log('fourth');
    expect(binarySearch([1, 2, 3, 4, 5, 6], 6)).toBe(true);
  });

  test('returns true if val is in the given array at the first index', function() {
    expect(binarySearch([1, 2, 3, 4, 5, 6], 1)).toBe(true);
  });

  test('returns false if val is not in the given array', function() {
    expect(binarySearch([1, 2, 3, 4, 5, 6], 10)).toBe(false);
  });

  test('returns false if no array is given', function() {
    expect(binarySearch(undefined, 1)).toBe(false);
  });

  test('returns false if no value is given', function() {
    expect(binarySearch([1, 2, 3], undefined)).toBe(false);
  });
});