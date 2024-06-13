
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


