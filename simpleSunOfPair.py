# Given an integer n, find two integers a and b such that:

# A) a >= 0 and b >= 0
# B) a + b = n
# C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.  
# You will return the digitSum(a) + digitsum(b).

# For example:
# solve(29) = 11. If we take 15 + 14 = 29 and digitSum = 1 + 5 + 1 + 4 = 11. There is no larger outcome.
# n will not exceed 10e10.

# More examples in test cases.

# Good luck!

def solve(n):
    if n < 10:
        return n
    a = int((len(str(n)) - 1) * '9')
    b = n - a
    return sum([int(i) for i in (list(str(a)) + list(str(b)))])


def solve(n):
    a = (len(str(n)) - 1) * '9' or '0'
    return sum(map(int, a + str(n - int(a))))import codewars_test as test
from solution import solve

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(solve(18),18)
        test.assert_equals(solve(29),11)
        test.assert_equals(solve(45),18)
        test.assert_equals(solve(1140),33)
        test.assert_equals(solve(7019),35)