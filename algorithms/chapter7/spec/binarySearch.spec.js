var binarySearch = require('../binarySearch').binarySearch;

describe('`binarySearch()`', function() {
  it('returns true if val is in the given array', function() {
    expect(binarySearch([1, 2, 3, 4, 5, 6], 4)).toBe(true);
  });

  it('returns false if val is not in the given array', function() {
    expect(binarySearch([1, 2, 3, 4, 5, 6], 10)).toBe(false);
  });

  it('returns false if no array is given', function() {
    expect(binarySearch(undefined, 1)).toBe(false);
  });

  it('returns false if no value is given', function() {
    expect(binarySearch([1, 2, 3], undefined)).toBe(false);
  });
});