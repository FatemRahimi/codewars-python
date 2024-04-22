# DESCRIPTION:
# 𝑖
# i is the imaginary unit, it is defined by 
# 𝑖
# ²
# =
# −
# 1
# i²=−1, therefore it is a solution to 
# 𝑥
# ²
# +
# 1
# =
# 0
# x²+1=0.

# Your Task
# Complete the function pofi that returns 
# 𝑖
# i to the power of a given non-negative integer in its simplest form, as a string (answer may contain 
# 𝑖
# i).

def pofi(n):
    if n % 4 == 0:
        return '1'
    
    if n % 4 == 1:
        return 'i'
    
    if n % 4 == 2:
        return '-1'
    
    return '-i'


#     even -1
#     odd  i
#     0    1
#     return 'i'

# another way
# def pofi(n):
#     return ['1','i','-1','-i'][n%4]


import codewars_test as test
from solution import pofi

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(pofi(0),'1')
        test.assert_equals(pofi(1),'i')
        test.assert_equals(pofi(2),'-1')
        test.assert_equals(pofi(3),'-i')
        test.assert_equals(pofi(4),'1')
        test.assert_equals(pofi(5),'i')
        test.assert_equals(pofi(6),'-1')
        test.assert_equals(pofi(7),'-i')
        test.assert_equals(pofi(8),'1')
        test.assert_equals(pofi(9),'i')
        test.assert_equals(pofi(10),'-1')