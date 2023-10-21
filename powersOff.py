# 

def pofi(n):
    return ('1','i','-1','-i')[n%4]

# test

import codewars_test as test
from solution import pofi

@test.describe("Basic Tests")
def basic_tests():
    