# # 
# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

# Example:
# For input: [3, 4, 4, 3, 6, 3]

# remove the 3 at index 0
# remove the 4 at index 1
# remove the 3 at index 3
# Expected output: [4, 6, 3]

# More examples can be found in the test cases.

# Good luck!

def solve(arr): 
    re = []
    for i in arr[::-1]:
        if i not in re:
            re.append(i)
    return re[::-1]

import codewars_test as test
from solution 
import solve

# test


@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(solve([3,4,4,3,6,3]),[4,6,3])
        test.assert_equals(solve([1,2,1,2,1,2,3]),[1,2,3])
        test.assert_equals(solve([1,2,3,4]),[1,2,3,4])
        test.assert_equals(solve([1,1,4,5,1,2,1]),[4,5,2,1])