
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