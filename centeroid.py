# Write a function centroid(c) to calculate the centroid of 3D coordinates.

# Return the results as a list of floats. Round the values to two decimal places.

import numpy as np

def centroid(c):
    return np.mean(c, axis=0).round(2).tolist()

# test

import codewars_test as test
from solution import centroid

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(centroid([[1,0,5], [0,1,5], [2,2,5]]), [1.0, 1.0, 5.0])
        test.assert_equals(centroid([[7,0,5], [3,1,5], [2,1,5]]), [4.0, 0.67, 5.0])