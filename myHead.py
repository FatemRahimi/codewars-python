# You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!

# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

# Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics

# Simples!

def fix_the_meerkat(arr):
    arr.reverse()
    return arr

def fix_the_meerkat(arr):
    temp = arr[0]
    arr[0] = arr[2]
    arr[2]= temp
    return arr
import codewars_test as test
from solution import fix_the_meerkat

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
        test.assert_equals(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
        test.assert_equals(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
        test.assert_equals(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
        test.assert_equals(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])g