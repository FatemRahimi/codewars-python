# It's based on this kata. It's suggested that you solve that kata first.

# Task
# You are given the length and width of a 4 sided polygon. The polygon can either be a rectangle or a square.

# Your job is to check if it is a square then return the area. If it is a rectangle then return its perimeter.

# Test.assertEquals(area_or_perimeter(6 , 10) , 32);
# Note
# Note : For the purposes of Kata you will assume that it is a square when lengths are equal otehrwise it is a rectangle.

# Code Limit
# code.length < 39 characters.

# Advice: if your code length is much longer than the limit, giving up is also a good choice :D



areaOrPerimeter=(h,w)=>h^w?2*(h+w):w*w




const Test = require('@codewars/test-compat');

describe("Basic Tests", function(){ 
it("It should works for basic tests.", function(){

Test.assertEquals(areaOrPerimeter(4 , 4) , 16);
Test.assertEquals(areaOrPerimeter(6 , 10) , 32);

})})