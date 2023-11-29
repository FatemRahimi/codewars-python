# The code provided is supposed replace all the dots . in the specified String str with dashes -

# But it's not working properly.

# Task
# Fix the bug so we can all go home early.

# Notes
# String str will never be null.

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)


import codewars_test as test
from solution import replace_dots

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(replace_dots(""), "")
        test.assert_equals(replace_dots("no dots"), "no dots")
        test.assert_equals(replace_dots("one.two.three"), "one-two-three")
        test.assert_equals(replace_dots("........"), "--------")