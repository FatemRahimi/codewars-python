# DESCRIPTION:
# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?

# Example(Input --> Output)

# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

def add_length(str_):
    answer = []
    for word in str_.split():
        answer.append(word + ' ' + str(len(word)))
    return answer
import codewars_test as test
from solution import add_length

@test.describe("Add Length")
def basic_tests():
    @test.it("Sample Tests")
    def _():
        test.assert_equals(add_length('apple ban'),["apple 5", "ban 3"])
        test.assert_equals(add_length('you will win'),["you 3", "will 4", "win 3"])
        test.assert_equals(add_length('you'),["you 3"])
        test.assert_equals(add_length('y'),["y 1"])