# Getting the Minimum Absolute Difference
# Task
# Given an array of integers with at least 2 elements: a1, a2, a3, a4, ... aN

# The absolute difference between two array elements ai and aj, where i != j, is the absolute value of ai - aj.

# Return the minimum absolute difference (MAD) between any two elements in the array.

# Example
# For [-10, 0, -3, 1]

# the MAD is 1.

# Explanation:

# | -10 -    0  | = 10
# | -10 -  (-3) | =  7
# | -10 -    1  | = 11
# |   0 - (-10) | = 10
# |   0 -  (-3) | =  3
# |   0 -    1  | =  1
# |  -3 - (-10) | =  7
# |  -3 -    0  | =  3
# |  -3 -    1  | =  4
# |   1 - (-10) | = 11
# |   1 -    0  | =  1
# |   1 -  (-3) | =  4
# The minimum value is 1 ( both | 0 - 1 | and | 1 - 0 | ).

# Note
# Note that the same value can appear more than once in the array. In that case, the MAD will be 0.


from itertools import combinations

def getting_mad(arr):
    return  min(abs(a-b) for a,b in combinations(arr,2))
  import codewars_test as test
from solution import getting_mad

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should return minimum absolute difference for simple cases")
    def basic_test_cases():
        arr = [-10,0,-3,1]
        res = 1
        test.assert_equals(getting_mad(arr), res)

    @test.it("should works for zero filled arr")
    def basic_test_cases():

        arr = [0,0,0,0]
        res = 0
        test.assert_equals(getting_mad(arr), res)

    @test.it("should works for positive and negative numbers")
    def basic_test_cases():

        arr = [-570, 542]
        res = 1112
        test.assert_equals(getting_mad(arr), res)

        arr = [-69, -808, 828, 57]
        res = 126
        test.assert_equals(getting_mad(arr), res)

        arr = [-425, -648, -371, 755, -140, -855, 277, 517, 667, 192, -409, -326]
        res = 16
        test.assert_equals(getting_mad(arr), res)

    @test.it("should return minimum absolute difference for positive numbers")
    def basic_test_cases():
        arr = [1,2,5,6,7]
        res = 1
        test.assert_equals(getting_mad(arr), res)

    @test.it("should return minimum absolute difference for negative numbers")
    def basic_test_cases():
        arr = [-1,-2,-5,-6,-7]
        res = 1
        test.assert_equals(getting_mad(arr), res)