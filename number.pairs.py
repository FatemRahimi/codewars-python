# In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.

# Note: Both arrays have the same dimensions.

# Example:

# arr1 = [13, 64, 15, 17, 88]
# arr2 = [23, 14, 53, 17, 80]
# get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
def get_larger_numbers(a, b):
    new = b
    for i in range(len(a)):
        if (a[i]>b[i]):
            new[i]=a[i]
    return new


# test
import codewars_test as test
from solution import get_larger_numbers

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = [13, 64, 15, 17, 88]
        b = [23, 14, 53, 17, 80]
        test.assert_equals(get_larger_numbers(a, b), [23, 64, 53, 17, 88], "Wrong result for a = {}, b = {}".format(a, b))
        a = [34, -64, 15, 17, 88]
        b = [23, 14, 53, 17, 80]
        test.assert_equals(get_larger_numbers(a, b), [34, 14, 53, 17, 88], "Wrong result for a = {}, b = {}".format(a, b))
