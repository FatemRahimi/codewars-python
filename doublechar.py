DESCRIPTION:
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!

def double_char(s):
    res = ''
    for i in s:
        res += i*2
    return res
#  test
import codewars_test as test
from solution import double_char

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(double_char("String"),"SSttrriinngg")
        test.assert_equals(double_char("Hello World"),"HHeelllloo  WWoorrlldd")
        test.assert_equals(double_char("1234!_ "),"11223344!!__  ")