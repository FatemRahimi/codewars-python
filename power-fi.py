# DESCRIPTION:
# 𝑖
# i is the imaginary unit, it is defined by 
# 𝑖
# ²
# =
# −
# 1
# i²=−1, therefore it is a solution to 
# 𝑥
# ²
# +
# 1
# =
# 0
# x²+1=0.

# Your Task
# Complete the function pofi that returns 
# 𝑖
# i to the power of a given non-negative integer in its simplest form, as a string (answer may contain 
# 𝑖
# i).

def pofi(n):
    if n % 4 == 0:
        return '1'
    
    if n % 4 == 1:
        return 'i'
    
    if n % 4 == 2:
        return '-1'
    
    return '-i'


#     even -1
#     odd  i
#     0    1
#     return 'i'

# another way
# def pofi(n):
#     return ['1','i','-1','-i'][n%4]