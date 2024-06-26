# DESCRIPTION:
# Your task is to find the next higher number (int) with same '1'- Bits.

# I.e. as much 1 bits as before and output next higher than input. Input is always an int in between 1 and 1<<30 (inclusive). No bad cases or special tricks...

# Some easy examples:
# Input: 129  => Output: 130 (10000001 => 10000010)
# Input: 127 => Output: 191 (01111111 => 10111111)
# Input: 1 => Output: 2 (01 => 10)
# Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)
# First some static tests, later on many random tests too;-)!

# Hope you have fun! :-)


def next_higher(x):
    next = 0
    if(x):
        rightOne = x & -(x)
        nextHigherOneBit = x + rightOne
        rightOnesPattern = x ^ nextHigherOneBit    
        rightOnesPattern = rightOnesPattern / rightOne
        rightOnesPattern = int(rightOnesPattern) >> 2
        next = nextHigherOneBit | rightOnesPattern
    return next



import codewars_test as test
from solution import next_higher

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(next_higher(128), 256, "next_higher(128)")
        test.assert_equals(next_higher(1), 2, "next_higher(1)")
        test.assert_equals(next_higher(1022), 1279, "next_higher(1022)")
        test.assert_equals(next_higher(127), 191, "next_higher(127)")
        test.assert_equals(next_higher(1253343), 1253359, "next_higher(1253343)")