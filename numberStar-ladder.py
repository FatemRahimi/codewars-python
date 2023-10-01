# Task
# Using n as a parameter in the function pattern, where n>0, complete the codes to get the pattern (take the help of examples):

# Note: There is no newline in the end (after the pattern ends)

# Examples
# pattern(3) should return "1\n1*2\n1**3", e.g. the following:

# 1
# 1*2
# 1**3
def pattern(n):
    s = ''
    for i in range(n):
        if i == 0:
            s += '1\n'
        else:
            s += '1{}{}\n'.format('*' * i, i + 1)
    
    return s.rstrip('\n')