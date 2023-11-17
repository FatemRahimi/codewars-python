# Description
# Peter enjoys taking risks, and this time he has decided to take it up a notch!

# Peter asks his local barman to pour him n shots, after which Peter then puts laxatives in x of them. He then turns around and lets the barman shuffle the shots. Peter approaches the shots and drinks a of them one at a time. Just one shot is enough to give Peter a runny tummy. What is the probability that Peter doesn't need to run to the loo?

# Task
# You are given:

# n - The total number of shots.

# x - The number of laxative laden shots.

# a - The number of shots that peter drinks.

# return the probability that Peter won't have the trots after drinking. n will always be greater than x, and a will always be less than 
function getChance(n, x, a){ 
  let event = n - x;
  let probability = 1;
  
  //conditional and combined probability
  for (let i = 0; i < a; i++) {
    probability *= (event / n);
    n--;
    event--;
  }
  return N

#   tested

  describe("testsSuite", function () {
    const { approximately } = require('chai').assert;

    function doTest(n, x, a, expected) {
        const actual = getChance(n, x, a);
        const message = `for n = ${n}, x = ${x}, a = ${a}\n`;
        approximately(actual, expected, 1e-9, message);
    }

    it("sampleTests", function () {
        doTest(  2,  1,  1, 0.5);
        doTest(  4,  1,  3, 0.25);
        doTest(100, 10, 10, 0.33);
    });
});