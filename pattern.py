# Here your task is to Create a (nice) Christmas Tree.

# You don't have to check errors or incorrect input values, every thing is ok without bad tricks, only one int parameter as input and a string to return;-)...

# So what to do?

# First three easy examples:

# Input: 3 and Output:
#   *
#  ***
# *****
#  ###
 
#  Input 9 and Output:
#     *
#    ***
#   *****
#    ***
#   *****
#  *******
#   *****
#  *******
# *********
#    ###
   
#  Input 17 and Output:
#       *
#      ***
#     *****
#      ***
#     *****
#    *******
#     *****
#    *******
#   *********
#    *******
#   *********
#  ***********
#   *********
#  ***********
# *************
#      ###
     
# Really nice trees, or what???! So merry Christmas;-)
# You can see, always a root, always steps of hight 3, tree never smaller than 3 (return "") and no difference for input values like 15 or 17 (because (int) 15/3 = (int) 17/3). That's valid for every input and every tree. Lines are delimited by \r\n and no trailing white space allowed. I think there's nothing more to say - perhaps look at the testcases too;-)!

# There are some static tests at the beginning and many random tests if you submit your solution.

def christmas_tree(height: int) -> str:
    if height < 3:
        return ''

    lines = []
    for i in range(1, height // 3 * 2 + 1, 2):
        for j in range(i, i + 6, 2):
            lines.append('*' * j)

    line_width = len(lines[-1])
    lines.append('###')
    return '\r\n'.join(line.center(line_width).rstrip() for line in lines)