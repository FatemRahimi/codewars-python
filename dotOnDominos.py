
# To earn a huge capital, you need to have an unconventional mindset. Of course, with such a complex job, there must also be special mechanisms for recreation and entertainment. For this purpose, the casino came up with a special domino set. Ordinary dominoes are a set of different combinations of two tiles, each displaying 0 to 6 points. And this set is a similar combination of tiles, but the number of points on each can be from zero to a set value that depends on the intellectual level of the players. There are all kinds of tile combinations in this dice set, but none of them must be repeated (combinations such as 2 | 5 and 5 | 2 are considered the same).there's a domino, don't worry :)When making this set of dominoes, the manufacturer faced the problem of counting the total number of points on all dominoes. This is due to the fact that the dominoes are decorated with diamonds, which are dots on the tiles and the cost of which must be estimated during manufacture.

# Input data:

# The function receives a parameter n, which indicates the maximum number of points on one domino tile.

# Test values are 0 < n < 1000

# Output data:

# Your function should return the optional number of diamond stones to be made for a given set of dice.

# Example:

# For dominoes where the maximum possible number on the knuckle is 2, the possible knuckles will be as follows --> 0 | 1, 0 | 2, 1 | 1, 1 | 2, 2 | 2 therefore, the sum of all values on the knuckles will be 1 + 2 + 1 + 1 + 1 + 2 + 2 + 2 = 12

# 2 --> 12
# 3 --> 30
# 20 --> 4620
# Help me write a program that solves this problem.



function dotsOnDominoBones(n){
     let result = 0 ;
   for(let i = 1 ; i <=n ;i++){
    result += (i * n) + (i * 2)
   }
   return result
}
# tested
const Test = require('@codewars/test-compat');

describe("Basic Test:", function() {
  it("tests", function() {
    Test.assertEquals(dotsOnDominoBones(2), 12);
    Test.assertEquals(dotsOnDominoBones(5), 105);
    Test.assertEquals(dotsOnDominoBones(13), 1365);
    Test.assertEquals(dotsOnDominoBones(20), 4620);
    Test.assertEquals(dotsOnDominoBones(33), 19635);
    Test.assertEquals(dotsOnDominoBones(50), 66300);
    Test.assertEquals(dotsOnDominoBones(0), 0);
    Test.assertEquals(dotsOnDominoBones(137), 1313967);
    Test.assertEquals(dotsOnDominoBones(198), 3940200);
  });
});



# If someone is interested, you can read the rules of the domino game here ;) Domino game

# If you have the desire or time, I would be very grateful if you can help in the development of this kata, to translate, or whatever else with me can be contacted via Telegram