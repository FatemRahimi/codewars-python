# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)
def hero(bullets, dragons):
    '''
    Ascertains if hero can survive
    Parameters:
        bullets: (int) - number of bullets hero has
        dragons: (int) - number of dragons
    Returns:
        True (Survive) or False (Hero gets killed)
    '''
    if bullets >= 2*dragons:
        return True
    elif bullets < 2*dragons:
        return False
    import codewars_test as test

    
from solution import hero

# tested

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hero(10, 5), false)
        test.assert_equals(hero(7, 4), False)
        test.assert_equals(hero(4, 5), False)
        test.assert_equals(hero(100, 40), True)
        test.assert_equals(hero(1500, 751), False)
        test.assert_equals(hero(0, 1), False)
