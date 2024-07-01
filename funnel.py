# Imagine a funnel filled with letters. The bottom letter drops out of the funnel and onto a conveyor belt:

#   \b,c/  -->   \b,c/
#    \a/   -->    \ /
#                  a
# -------     -------
# If there are two letters above a gap, the smaller letter falls into the gap.

#   \b,c/   -->   \  c/ 
#    \ /    -->    \b/   
# a            a         
# -------      -------
# Of course, this can create a new gap, which must also be filled in the same way:

#   \f,e,d/  -->  \f, ,d/
#    \  c/   -->   \e,c/ 
#     \b/           \b/   
#    a            a         
#   -------      -------
# Once all the gaps above it have been filled, the bottom letter drops out of the funnel and onto the conveyorbelt. The process continues until all letters have fallen onto the conveyor. (New letters fall onto the end of the existing string)

# KATA GOAL: Return the string on the conveyorbelt after all letters have fallen.

# \f, ,d/      \f, ,d/   --> etc -->    \     /
#  \e,c/        \e,c/    --> etc -->     \   /
#   \b/    -->   \ /     --> etc -->      \ /
# a           a   b                   abcdef
# -------     -------                 -------
# All letters in the funnel will be unique i.e. in every comparison one letter will be strictly smaller than the other. The funnel will be presented as a nested list, e.g:

# [["d","a","c"],
#    ["b","e"],
#      ["f"]]
# The value of a letter is defined by its codepoint. Note: this means all capital letters are defined as smaller than all lower-case letters, but your language's comparison operator will probably treat it that way automatically.

# The funnels will always be "nice" -- every layer will have 1 item more than the layer below, and every layer will be full, and generally there's no funny business or surprises to consider. The only characters used are standard uppercase and lowercase letters A-Z and a-z. The tests go up to 9 layer funnel.

# Fully Worked Example
# \d,a,c/      \d,a,c/      \d,a,c/ -->  \d   c/     
#  \b,e/        \b,e/  -->   \  e/  -->   \a,e/
#   \f/   -->    \ /   -->    \b/          \b/  --> 
#                 f        f            f
# ------      -------      -------      -------


# \d   c/      \d   c/ -->  \    c/      \    c/     
#  \a,e/  -->   \  e/  -->   \d,e/        \d,e/  -->
#   \ /   -->    \a/          \a/   -->    \ /   -->
# f  b        fb           fb           fb  a
# ------      -------      -------      -------


#  \    c/      \    c/      \    c/ -->  \     /     
#   \  e/        \  e/  -->   \   /  -->   \  c/   
#    \d/   -->    \ /   -->    \e/          \e/  -->
# fba          fba d       fbad          fbad
# -------      -------     --------      -------


#   \     /      \     /      \     /
#    \  c/  -->   \   /        \   / 
#     \ /          \c/   -->    \ /   
# fbad e       fbade        fbadec         
# -------      -------      -------

# DONE. Return "fbadec".


from copy import deepcopy

def funnel_out(funnel: list) -> str:
    funnel = deepcopy(funnel)
    depth = len(funnel)
    return ''.join(drip(funnel, -1, 0) for _ in range(depth * (depth + 1) // 2))

def drip(funnel: list, row: int, col: int) -> str:
    if funnel[row][col] == '~': return '~'
    result = funnel[row][col]
    if abs(row) == len(funnel):
        funnel[row][col] = '~'
    elif funnel[row - 1][col] > funnel[row - 1][col + 1]:
        funnel[row][col] = drip(funnel, row - 1, col + 1)
    else:
        funnel[row][col] = drip(funnel, row - 1, col)
    return result


test.assert_equals(funnel_out([["q"]]),"q")
test.assert_equals(funnel_out([["b","c"],["a"]]),"abc")
test.assert_equals(funnel_out([["d","a","c"],["b","e"],["f"]]),"fbadec")
test.assert_equals(funnel_out([["a","e","c","f"],["d","i","h"],["j","g"],["b"]]),"bghcfiejda")