# Given an array (a list in Python) of integers and an integer n, find all occurrences of n in the given array and return another array containing all the index positions of n in the given array.

# If n is not in the given array, return an empty array [].

# Assume that n and all values in the given array will always be integers.

# Example:

# find_all([6, 9, 3, 4, 3, 82, 11], 3)
# > [2, 4]

def find_all(array, n):
    res = []
    for i in range(len(array)):
        if array[i] == n:
            res.append(i)
    return res
# test

import codewars_test as test
from solution import find_all

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_all([6, 9, 3, 4, 3, 82, 11], 3), [2, 4])
        test.assert_equals(find_all([6, 9, 3, 4, 3, 82, 11], 99), [])
        test.assert_equals(find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16), [1, 9])
        test.assert_equals(find_all([20, 20, 10, 13, 15, 2, 7, 2, 20, 3, 18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5], 20), [0, 1, 8])