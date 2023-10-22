# Count how often sign changes in array.

# result
# number from 0 to ... . Empty array returns 0

# example
# const arr = [1, -3, -4, 0, 5];

# /*
# | elem | count |
# |------|-------|
# |  1   |  0    |
# | -3   |  1    |
# | -4   |  1    |
# |  0   |  2    |
# |  5   |  2    |
# */

# catchSignChange(arr) == 2;

def catch_sign_change(lst):
    count = 0
    for i in range(1,len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:count += 1
        if lst[i] >= 0 and lst[i-1] < 0:count += 1
    return count
# tested

import codewars_test as test
from solution import catch_sign_change

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(catch_sign_change([-7,-7,7,0]), 1)
        test.assert_equals(catch_sign_change([1,5,2,-4]), 1)
        test.assert_equals(catch_sign_change([-8,4,-1,5,-3,-3,-2,-2]), 4)
        test.assert_equals(catch_sign_change([-2,-2,-5,-4,5,2,0,6,0]), 1)
        test.assert_equals(catch_sign_change([2,6,3,0,5,-3]), 1)
        test.assert_equals(catch_sign_change([-3,3]), 1)
        test.assert_equals(catch_sign_change([-1,2,2,2,2,-8,-1]), 2)
        test.assert_equals(catch_sign_change([1,-2,-7,-4,4,-2,0,-3,3]), 6)
        test.assert_equals(catch_sign_change([3,7,-6,2,3,1,1]), 2)
        test.assert_equals(catch_sign_change([13,-7,-6,2,-1,1,-1]), 5)
    
    @test.it('It should pass fixed tests with zero changes')
    def basic_test_cases():
        test.assert_equals(catch_sign_change([]), 0)
        test.assert_equals(catch_sign_change([0]), 0)
        test.assert_equals(catch_sign_change([4,1]), 0)
        test.assert_equals(catch_sign_change([-1, -2, -3]), 0)