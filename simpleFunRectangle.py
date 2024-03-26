# DESCRIPTION:
# Task
# Imagine n horizontal lines and m vertical lines.

# Some of these lines intersect, creating rectangles.

# How many rectangles are there?

# Examples
# For n=2, m=2, the result should be 1.

# there is only one 1x1 rectangle.

# For n=2, m=3, the result should be 3.

# there are two 1x1 rectangles and one 1x2 rectangle. So 2 + 1 = 3.

# For n=3, m=3, the result should be 9.

# there are four 1x1 rectangles, two 1x2 rectangles, two 2x1 rectangles and one 2x2 rectangle. So 4 + 2 + 2 + 1 = 9.

# Input & Output
# [input] integer n

# Number of horizontal lines.

# Constraints: 0 <= n <= 100

# [input] integer m

# Number of vertical lines.

# Constraints: 0 <= m <= 100

# [output] an integer

# Number of rectangles.

def rectangles(n, m):
  return n*m*(n-1)*(m-1)//4

def rectangles(n, m):
    s = lambda x: (1+x)*x//2
    n -= 1; m -= 1
    return s(n) * s(m)

import codewars_test as test
from solution import rectangles

@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(rectangles(2,3),3)
        test.assert_equals(rectangles(2,2),1)
        test.assert_equals(rectangles(1,1),0)
        test.assert_equals(rectangles(0,1),0)
        test.assert_equals(rectangles(3,3),9)
        test.assert_equals(rectangles(100,100),24502500)