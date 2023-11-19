# Given two arrays, a1 and a2, sort the elements of a2 based on the the index of the word in a1 that begins with the same letter.

# Example 1
# a1 = ['giraffe', 'orangutan', 'impala', 'elephant', 'rhino']
# a2 = ['rattlesnake', 'eagle', 'geko', 'iguana', 'octopus']

# returns ['geko', 'octopus', 'iguana', 'eagle', 'rattlesnake']
# Example 2
# a1 = ['jellyfish', 'koi', 'caribou', 'owl', 'dolphin']
# a2 = ['ostrich', 'jaguar', 'deer', 'camel', 'kangaroo']

# returns ['jaguar', 'kangaroo', 'camel', 'ostrich', 'deer']
# Each element in the arrays will start with a unique letter so there will only be a single match for each element.

# test
function sortArray(a1, a2) {
    let newArr = [];
    for(let i = 0; i < a1.length; i++) { 
        for(let j = 0; j < a2.length; j++) {
            if(a2[j][0] === a1[i][0]) newArr.push(a2[j])       
        }
    }
    return newArr
}
const chai = require("chai")
const assert = chai.assert
chai.config.truncateThreshold = 0

describe("Tests", () => {
  it("test", () => {
var a1 = ['giraffe', 'orangutan', 'impala', 'elephant', 'rhino'];
var a2 = ['rattlesnake', 'eagle', 'geko', 'iguana', 'octopus'];
assert.deepEqual(sortArray(a1, a2), ['geko', 'octopus', 'iguana', 'eagle', 'rattlesnake']);

var a1 = ['jellyfish', 'koi', 'caribou', 'owl', 'dolphin'];
var a2 = ['ostrich', 'jaguar', 'deer', 'camel', 'kangaroo'];
assert.deepEqual(sortArray(a1, a2), ['jaguar', 'kangaroo', 'camel', 'ostrich', 'deer']);

var a1 = ['newt', 'lizard', 'snail', 'tapir', 'rabbit'];
var a2 = ['tortoise', 'narwhal', 'llama', 'raven', 'sloth'];
assert.deepEqual(sortArray(a1, a2), ['narwhal', 'llama', 'sloth', 'tortoise', 'raven']);
  });
});