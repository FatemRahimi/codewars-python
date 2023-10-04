# Complete the function which converts hex number (given as a string) to a decimal number.
def hex_to_dec(s):
    key = "0123456789abcdef"
    n=0
    res=0
    for l in s[::-1]:
        res += key.index(l)*(16.**n)
        n+=1
        
    return int(res)

# test
import codewars_test as test
from solution import hex_to_dec

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hex_to_dec("1"), 1)
        test.assert_equals(hex_to_dec("a"), 10)
        test.assert_equals(hex_to_dec("10"), 16)