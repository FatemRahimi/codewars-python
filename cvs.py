
# Create a function that returns the CSV representation of a two-dimensional numeric array.

# Example:

# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]] 
    
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'

toCsvText = lambda a: '\n'.join([','.join([str(e) for e in r]) for r in a])

# test

import codewars_test as test
from solution import to_csv_text


@test.it("Basic tests")
def _():
    test.assert_equals(
        to_csv_text([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ]),
        "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",
    )
