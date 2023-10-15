# Tim's Fruit Shop Challenge
# Tim runs a fruit shop, and he has a unique way of processing orders. Customers send orders in a specific format: they specify the number of fruit units they want, followed by a lowercase letter (a-z) representing the fruit itself. For example, '30a4b' means 30 apples and 4 bananas.

# Tim's task is to organize these orders into packages. Here's how he does it:

# Every 10 units of a fruit go into a box, represented by {a}.
# Every 5 boxes are stacked into a pallet, represented by [a].
# Any remaining units are put into a bag, enclosed by ().
# Then he prepares every order in a 3 tier shelf (list) with the pallets on the lower tier, the boxes on medium tier and the bags on the upper tier. the items will be pushed to the right and the empy space filled with '-'

# Explained example:
#   '63a21b'
#      =
#    '63a' : 50 * 1 + 10 * 1 + 3 -> '[a]{a}(aaa)'  
#      +
#    '21b' : 50 * 0 + 10 * 2 + 1 -> '{b}{b}(b)' 
    
    
#   '63a21b' -> '[a]{a}(aaa){b}{b}(b)'
  
  
# Then the products should be stored in the shelf as follows:

#  ['-(aaa)(b)',
#   '{a}{b}{b}',
#   '------[a]']
# You will help Tim prepare or the daily orders in selves.

# Input
# A list containing all the orders for the day. It will be a list of strings. Each order(string) containing maximun one repetition of each fruit (letter from a to z) preceded by the corresponding amount. The list will contain at least one amount item combination

# output
# A list containing a list for each shelf containing a list for each tier

# Examples:
#                          [['-(aaa)(b)',
#            ["63a21b"] ->   '{a}{b}{b}',
#                           '------[a]']]
          
#                           [['---',
#               ['10a'] ->    '{a}',
#                             '---']] 
                           
#                          [['(bbb)',
#                            '--{a}',
# ['10a3b', '64j1k92i'] ->   '-----'],
#                          ['--(jjjj)(k)(ii)',
#                           '{j}{i}{i}{i}{i}',
#                           '---------[j][i]']]
          
       fruit_pack=lambda a:list(map(f,a))

def f(s):
    L=["","",""]
    n=o=""
    for c in s:
        if c.isdigit(): n+=c
        else:
            n=int(n)
            a,n=divmod(int(n),50)
            L[2]+=f"[{c}]"*a
            a,n=divmod(int(n),10)
            L[1]+=f"{{{c}}}"*a
            if n: L[0]+=f"({c*n})"
            n=""
    return [x.rjust(max(map(len,L)),'-')for x in L]