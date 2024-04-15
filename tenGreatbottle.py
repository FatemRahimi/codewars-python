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
    dict1 = {1:'One green bottle',2:'Two green bottles',3:'Three green bottles',4:'Four green bottles',5:'Five green bottles',6:'Six green bottles',7:'Seven green bottles',8:'Eight green bottles',9:'Nine green bottles',10:'Ten green bottles'}
    list1 = []
    while n != 0:
        if n == 1:
            str1 = "One green bottle hanging on the wall,\nOne green bottle hanging on the wall,\nIf that one green bottle should accidentally fall,\nThere'll be no green bottles hanging on the wall.\n"
        else:
            str1 = f"{dict1[n]} hanging on the wall,\n{dict1[n]} hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {dict1[n - 1].lower()} hanging on the wall.\n\n"
        n = n - 1
        list1.append(str1)
    return ''.join(list1)


