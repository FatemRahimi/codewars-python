# Task
# Given Two integers a , b , find The sum of them , BUT You are not allowed to use the operators + and -

# Notes
# The numbers (a,b) may be positive , negative values or zeros .

# Returning value will be an integer .

# Input >> Output Examples
# 1- Add (5,19) ==> return (24) 

# 2- Add (-27,18) ==> return (-9)

# 3- Add (-14,-16) ==> return (-30)


def add(x, y):
    if y == 0:
        return x
    return add(x ^ y, (x & y) << 1)
