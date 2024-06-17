
# Create a function

# has_two_cube_sums(n)
# which checks if a given number n can be written as the sum of two cubes in two different ways: n = a³+b³ = c³+d³. All the numbers a, b, c and d should be different and greater than 0.

# E.g. 1729 = 9³+10³ = 1³+12³.

# has_two_cube_sums(1729); // true
# has_two_cube_sums(42);   // false



def has_two_cube_sums(n):
    sum = []
    power = int(n ** (1/3.0))+1
    for i in xrange(1, power):
        for x in xrange(1, power):
            if i == x:
                continue
            tmp = i**3 + x**3
            if tmp > n: 
               break
            if tmp == n:
                if len(sum) == 2:
                    return True
                sum.append([i , x])
    return False



test.assert_equals(has_two_cube_sums(1), False)
test.assert_equals(has_two_cube_sums(1729),True) # 9^3 + 10^3 and 1^3 + 12^3
test.assert_equals(has_two_cube_sums(42), False)
test.assert_equals(has_two_cube_sums(4104), True)
test.assert_equals(has_two_cube_sums(4105), False)