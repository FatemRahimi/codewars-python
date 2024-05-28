# import math

def cooking_time(needed_power, minutes, seconds, power):
    needed_power = int(needed_power[:-1])
    power = int(power[:-1])
    time = minutes * 60 + seconds
    res_time = math.ceil(time * needed_power / power)
    return "{0} minutes {1} seconds".format(res_time // 60, res_time % 60)

import codewars_test as test
from solution import cooking_time

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(cooking_time("600W", 4, 20, "800W"), "3 minutes 15 seconds")
        test.assert_equals(cooking_time("800W", 3, 0, "1200W"), "2 minutes 0 seconds")
        test.assert_equals(cooking_time("100W", 8, 45, "50W"), "17 minutes 30 seconds")
        test.assert_equals(cooking_time("7500W", 0, 5, "600W"), "1 minutes 3 seconds")
        test.assert_equals(cooking_time("450W", 3, 25, "950W"), "1 minutes 38 seconds")
        test.assert_equals(cooking_time("21W", 64, 88, "25W"), "55 minutes 0 seconds")
        test.assert_equals(cooking_time("83W", 61, 80, "26W"), "199 minutes 0 seconds")
        test.assert_equals(cooking_time("38W", 95, 22, "12W"), "302 minutes 0 seconds")
        