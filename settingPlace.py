
# This kata is a submission to the EPIC Challenge 2024.

# The Hall
# You are a servant in The Great Hall of Ghosts. The purpose of this place is to hold the Day of Passing ceremony in honor of the deceased members of your society. The hall was carved directly out of the mountain rock to house a majestic square Grand Table surrounded by twelve magnificent Seats of Honor. Each corner of the hall is adorned by one of the four Culturally Significant Features. Going clockwise around the table, they are; a comforting arrangement of earthenware holding exotic plants in lucious soil, a natural waterfall of gentle sounds and sweet moisture, a roaring fireplace of tremendous warmth, and a breezy windowsill open to the freshest of air.

# Earthenware                            Waterfall

#      ( __1__ ) ( __2__ ) ( __3__ ) ( __4__ )

#      ( _12__ )                     ( __5__ )

#      ( _11__ )                     ( __6__ )

#      ( _10__ ) ( __9__ ) ( __8__ ) ( __7__ )

#  Windowsill                             Fireplace
# The Dead
# Every morning, the Elders give you a List of the Dead naming people who throughout the past had died on that date, although a person's name is only included on the list if currently living members of society have made any donations in their name for this year.

# Your Task


CORNERS = {letter: 3 * i for i, letters in enumerate(("QUTHCRDMZ", "WEVOXING", "JFABKPLY", "S")) for letter in letters}

def set_table(the_dead):
    n = 12
    table = ['_____'] * n
    def find_seat(i, d):
        for j in range(n):
            k = (i + d * j) % n
            if table[k] == '_____':
                return k, j
    for name in the_dead[:12]:
        p = CORNERS[name[0]]
        p1, d1 = find_seat(p, -1)
        p2, d2 = find_seat(p, 1)
        table[p1 if d1 <= d2 else p2] = name
    return table


from solution import set_table
import codewars_test as test

@test.describe("set_table")
def tests():

    @test.it("Sample Tests")
    def sample_tests():

        # Test 1 ~ Artlu only
        the_dead = ("Artlu",)
        submitted = set_table(the_dead)
        expected = ["_____", "_____", "_____", "_____", "_____", "_____", "Artlu", "_____", "_____", "_____", "_____", "_____"]
        test.assert_equals(submitted, expected)
        
        # Test 2 ~ Artlu, Breca, Cityl, and Dedaf
        the_dead = ("Artlu", "Breca", "Cityl", "Dedaf")
        submitted = set_table(the_dead)
        expected = ["Cityl", "_____", "_____", "_____", "_____", "Breca", "Artlu", "_____", "_____", "_____", "_____", "Dedaf"]
        test.assert_equals(submitted, expected)
        
        # Test 3 ~ All Favor the Same Feature
        the_dead = ("Sevap", "Syolc", "Sgulg", "Stolb", "Sknoh", "Spord", "Sgnaf", "Shcat", "Sknit", "Snirg", "Senin", "Sliob")    
        submitted = set_table(the_dead)
        expected = ["Sgnaf", "Sknit", "Senin", "Sliob", "Snirg", "Shcat", "Spord", "Stolb", "Syolc", "Sevap", "Sgulg", "Sknoh"]
        test.assert_equals(submitted, expected)
        
        # Test 4 ~ Example From the Description
        the_dead = ["Yojne", "Xenna", "Verap", "Ebyam", "Teseb", "Ycuag", "Onets", "Skcaw", "Yrovi", "Tpets", "Lizuf", "Girnu"]
        submitted = set_table(the_dead)
        expected = ["Teseb", "Onets", "Verap", "Xenna", "Ebyam", "Ycuag", "Yojne", "Yrovi", "Lizuf", "Skcaw", "Girnu", "Tpets"]
        test.assert_equals(submitted, expected)
        
        # Test 5 ~ Too Many Ghosts to Seat
        the_dead = ['Egdob', 'Liame', 'Skceg', 'Yesba', 'Cinid', 'Sallo', 'Sumac', 'Triks', 'Sipat', 'Elona', 'Sreod', 'Deyab', 'Dlaps', 'Nevey', 'Htron']
        submitted = set_table(the_dead)
        expected = ["Cinid", "Sreod", "Elona", "Egdob", "Deyab", "Yesba", "Liame", "Sipat", "Sallo", "Skceg", "Sumac", "Triks"]
        test.assert_equals(submitted, expected)
