# DESCRIPTION:
# Who knows the nursery rhyme Ten Green Bottles?

# Lyrics:

# Ten green bottles hanging on the wall,
# Ten green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There'll be nine green bottles hanging on the wall.

# Nine green bottles hanging on the wall,
# Nine green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There'll be eight green bottles hanging on the wall. 

# Eight green bottles hanging on the wall...
# Seven green bottles hanging on the wall...
# ...

# One green bottle hanging on the wall,
# One green bottle hanging on the wall,
# If that one green bottle should accidentally fall,
# There'll be no green bottles hanging on the wall.
# Task
# Write some amazing code to reproduce the above lyrics starting from n green bottles!

# parameter n is 1 to 10
# newline terminates every line (including the last)
# don't forget the blank lines between the verses

def ten_green_bottles(n):
    numbers = {10: 'ten', 9: 'nine', 8: 'eight', 7: 'seven', 6: 'six', 5: 'five',
               4: 'four', 3: 'three', 2: 'two', 1: 'one', 0: 'no'}
    res = []
    for x in range(n, 0, -1):
        s = f"""{numbers[x].capitalize()} green bottle{'s' if x > 1 else ''} hanging on the wall,
{numbers[x].capitalize()} green bottle{'s' if x > 1 else ''} hanging on the wall,
{'And if' if x > 1 else "If that"} one green bottle should accidentally fall,
There'll be {numbers[x-1]} green bottle{'' if x-1 == 1 else 's'} hanging on the wall.
"""
        res.append(s)
    return '\n'.join(res)


import codewars_test as test
from solution import ten_green_bottles

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        expected = "Two green bottles hanging on the wall,\n"\
        "Two green bottles hanging on the wall,\n"\
        "And if one green bottle should accidentally fall,\n"\
        "There'll be one green bottle hanging on the wall.\n"\
        "\n"\
        "One green bottle hanging on the wall,\n"\
        "One green bottle hanging on the wall,\n"\
        "If that one green bottle should accidentally fall,\n"\
        "There'll be no green bottles hanging on the wall.\n"
        test.assert_equals(ten_green_bottles(2), expected)