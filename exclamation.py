# Description:
# Remove n exclamation marks in the sentence from left to right. n is positive integer.

# Examples
# remove("Hi!",1) === "Hi"
# remove("Hi!",100) === "Hi"
# remove("Hi!!!",1) === "Hi!!"
# remove("Hi!!!",100) === "Hi"
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"

def remove(s, n):
    liste=[]
    k=1
    for i in range(len(s)):
            if s[i]=="!" and k<=n:
                k+=1
            else:
                liste.append(s[i])
    return "".join(liste)

# test
import codewars_test as test
from solution import remove

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():

        tests = [
            #[[input], [expected]],
            [["Hi!",1] , "Hi"],
            [["Hi!",100] , "Hi"],
            [["Hi!!!",1] , "Hi!!"],
            [["Hi!!!",100] , "Hi"],
            [["!Hi",1] , "Hi"],
            [["!Hi!",1] , "Hi!"],
            [["!Hi!",100] , "Hi"],
            [["!!!Hi !!hi!!! !hi",1] , "!!Hi !!hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",3] , "Hi !!hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",5] , "Hi hi!!! !hi"],
            [["!!!Hi !!hi!!! !hi",100] , "Hi hi hi"],
        ]


        for inp, exp in tests:
            test.assert_equals(remove(*inp), exp)