# Our spaceship has crashed on an unknown planet many light years away from earth. Thankfully we were able to send out a distress signal right before the crash. Help will be here shortly but we need to gather as much information about this planet as we can before we're rescued.

# Before our control panels were destroyed, we were able to gather the duration of this planet's orbit around it's planetary system's star.

# Among other things, we need to determine if a given year is a leap year on this planet.

# Your Task:

# Given the duration of the planet's orbit (in days) and a specific year on this planet, determine if the given year is a leap year here.

# For example:

# On Earth, a single rotation around the sun takes 365.25 days. Therefore, each year takes 365 days but every forth year is a leap year and takes 366 days. The next leap year on Earth will occur in 2020.

# Notes: To make things easier, the period of the leap years will always be a power of 2. Good luck!

def is_leap_year(d, y):
    x = d % 1
    t = 1 / x 
    print(t)
    return y % t == 0


def is_leap_year(d, y):
    return (d * y) % 1 == 0


from solution import is_leap_year
import codewars_test as test

@test.describe("Leap years on a distant planet")
def leap_years_on_a_distant_planet():
    
    @test.it("Example tests")
    def example_tests():
        test.assert_equals(is_leap_year(365.25,  2018), False, '2018 is not a leap year on Earth')
        test.assert_equals(is_leap_year(365.25,  2020), True,  '2020 is a leap year on Earth')
        test.assert_equals(is_leap_year(124.5,    102), True,  '102 is a leap year on this planet')
        test.assert_equals(is_leap_year(124.125,  102), False, '102.125 is not a leap year this planet')