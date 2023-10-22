# Count how often sign changes in array.

# result
# number from 0 to ... . Empty array returns 0

# example
# const arr = [1, -3, -4, 0, 5];

# /*
# | elem | count |
# |------|-------|
# |  1   |  0    |
# | -3   |  1    |
# | -4   |  1    |
# |  0   |  2    |
# |  5   |  2    |
# */

# catchSignChange(arr) == 2;

def catch_sign_change(lst):
    count = 0
    for i in range(1,len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:count += 1
        if lst[i] >= 0 and lst[i-1] < 0:count += 1
    return count