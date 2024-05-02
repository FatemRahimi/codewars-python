# ""

def is_all_possibilities(arr):
    if arr == []:
        return False
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i:
            return False
    return True


import codewars_test as test
from solution import is_all_possibilities

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(is_all_possibilities([0,2,19,4,4]),False)
        test.assert_equals(is_all_possibilities([3,2,1,0]),True)
        test.assert_equals(is_all_possibilities([0,1,2,3]),True)
        test.assert_equals(is_all_possibilities([1,2,3,4]),False)
        test.assert_equals(is_all_possibilities([0,2,3]),False)
        test.assert_equals(is_all_possibilities([0]),True)
        test.assert_equals(is_all_possibilities([0,1,2,3,4,5,6,7,8,9]),True)
        test.assert_equals(is_all_possibilities([0,1,3,-2,5,4]),False)
        test.assert_equals(is_all_possibilities([1,-1,2,-2,3,-3,6]),False)