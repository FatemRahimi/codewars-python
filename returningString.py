
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# for python 3.6
# def greet(name):
#     return f'Hello, {name} how are you doing today?'


# def greet(name):
#     return 'Hello, ' + name + ' how are you doing today?'



# tested
import codewars_test as test
from solution import greet

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
