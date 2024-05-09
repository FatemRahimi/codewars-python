# Template Strings
# Template Strings, this kata is mainly aimed at the new JS ES6 Update introducing Template Strings
# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word ```' are '```def temple_strings(obj, feature): 
  
def temple_strings(obj, feature): 
    return obj+" are "+feature


import codewars_test as test
from solution import temple_strings

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(temple_strings("Animals","Good"), 'Animals are Good')
    test.assert_equals(temple_strings("Animals","Good"), 'Animals are Good')
    test.assert_equals(temple_strings("You","Special"), 'You are Special')
    test.assert_equals(temple_strings("lives","frozen"), 'lives are frozen')