# Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

function mergeArrays(a, b) {
    let merge = [...a, ...b].sort()
    let unique = new Set(merge)
    return Array.from(unique).sort((a,b)=> a-b)
}
Best Practices7Clever1
 0ForkCompare with your solutionLink

# tested
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold = 0;

describe("mergeArrays", function(){
  it("Example Tests", function(){
    assert.deepEqual(mergeArrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]);
    assert.deepEqual(mergeArrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8]);
  });
});