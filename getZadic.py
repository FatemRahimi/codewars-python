# Your task is to get Zodiac Sign using input day and month.

# For example:

# get_zodiac_sign(1,5) => 'Taurus'
# get_zodiac_sign(10,10) => 'Libra'
# Correct answers are (preloaded):

# SIGNS = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
# P.S. Each argument is correct integer number.

# WESTERN ASTROLOGY STAR SIGN DATES

# Aries (March 21-April 19)
# Taurus (April 20-May 20)
# Gemini (May 21-June 20)
# Cancer (June 21-July 22)
# Leo (July 23-August 22)
# Virgo (August 23-September 22)
# Libra (September 23-October 22)
# Scorpio (October 23-November 21)
# Sagittarius (November 22-December 21)
# Capricorn (December 22-January 19)
# Aquarius (January 20 to February 18)
# Pisces (February 19 to March 20)



ZODIAC = (
    (11, 119, "Capricorn", "1 January - 19 January"),
    (120, 218, "Aquarius", "20 January - 18 February"),
    (219, 320, "Pisces", "19 February - 20 March"),
    (321, 419, "Aries", "21 March - 19 April"),
    (420, 520, "Taurus", "20 April - 20 May"),
    (521, 620, "Gemini", "21 May - 20 June"),
    (621, 722, "Cancer", "21 June - 22 July"),
    (723, 822, "Leo", "23 July - 22 August"),
    (823, 922, "Virgo", "23 August - 22 September"),
    (923, 1022, "Libra", "23 September - 22 October"),
    (1023, 1121, "Scorpio", "23 October - 21 November"),
    (1122, 1221, "Sagittarius", "22 November - 21 December"),
    (1222, 1231, "Capricorn", "22 December - 31 December")
)

def get_zodiac_sign(day, month):
    interval = int(f"{month}" + f"{day:02d}")
    return next((zodiac[2] for zodiac in ZODIAC if zodiac[0] <= interval <= zodiac[1]), "Unknown")



import codewars_test as test
from solution import get_zodiac_sign

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_zodiac_sign(10,10), 'Libra', "Expected 'Libra'")
        test.assert_equals(get_zodiac_sign(1,5), 'Taurus', "Expected 'Taurus'")
        test.assert_equals(get_zodiac_sign(6,9), 'Virgo', "Expected 'Virgo'")
        test.assert_equals(get_zodiac_sign(25,11), 'Sagittarius', "Expected 'Sagittarius'")