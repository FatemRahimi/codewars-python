# Write a function that accepts two numbers a and b and returns whether a is smaller than, bigger than, or equal to b, as a string.

# (5, 4)   ---> "5 is greater than 4"
# (-4, -7) ---> "-4 is greater than -7"
# (2, 2)   ---> "2 is equal to 2"
# There is only one problem...

# You cannot use if statements, and you cannot use the ternary operator ? :.

# In fact the word if and the character ? are not allowed in your code.



# solution

def no_ifs_no_buts(a, b):
    result = {
        a == b: "equal to",
        a < b: "smaller than",
        a > b: "greater than",
    }[True]
    return f"{b} is {result} {b}"

# test
import codewars_test as test
from solution import no_ifs_no_buts

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(no_ifs_no_buts(45,51),"45 is smaller than 51")
        test.assert_equals(no_ifs_no_buts(1,2),"1 is smaller than 2")
        test.assert_equals(no_ifs_no_buts(-3,2),"-3 is smaller than 2")
        test.assert_equals(no_ifs_no_buts(1,1),"1 is equal to 1")
        test.assert_equals(no_ifs_no_buts(100,100),"100 is equal to 100")
        test.assert_equals(no_ifs_no_buts(100,80),"100 is greater than 80")
        test.assert_equals(no_ifs_no_buts(20,19),"20 is greater than 19")