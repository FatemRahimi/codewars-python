# A History Lesson
# The Pony Express was a mail service operating in the US in 1859-60.

# Pony Express
# It reduced the time for messages to travel between the Atlantic and Pacific coasts to about 10 days, before it was made obsolete by the transcontinental telegraph.

# How it worked
# There were a number of stations, where:

# The rider switched to a fresh horse and carried on, or
# The mail bag was handed over to the next rider
# Kata Task
# stations is a list/array of distances (miles) from one station to the next along the Pony Express route.

# Implement the riders method/function, to return how many riders are necessary to get the mail from one end to the other.

# NOTE: Each rider travels as far as he can, but never more than 100 miles.

def riders(stations):
    riders, travelled = 1, 0
    
    for dist in stations:
        if travelled + dist > 100:
            riders += 1
            travelled = dist
        else:
            travelled += dist
    
    return riders

@test.describe("Sample tests")
def testEx():
    test.assert_equals(riders([18, 15]), 1)
    test.assert_equals(riders([43, 23, 40, 13]), 2)
    test.assert_equals(riders([33, 8, 16, 47, 30, 30, 46]), 3)
    test.assert_equals(riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]), 4)