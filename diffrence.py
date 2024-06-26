# DESCRIPTION:
# The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

# The result array should be sorted in ascending order of values.

# Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

# Examples
# [1, 2, 3, 4]  should return [(1, 3), (2, 4)]

# [4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

# [1, 23, 3, 4, 7] should return [(1, 3)]

# [4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]
def twos_difference(arr):
    arr = sorted(arr)
    b = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] - arr[i] == 2:
                b.append((arr[i],arr[j]))
    return b
test.assert_equals(twos_difference([1, 2, 3, 4]), [(1, 3), (2, 4)])
test.assert_equals(twos_difference([1, 3, 4, 6]), [(1, 3), (4, 6)])
test.assert_equals(twos_difference([0, 3, 1, 4]), [(1, 3)])
test.assert_equals(twos_difference([4, 1, 2, 3]), [(1, 3), (2, 4)])
test.assert_equals(twos_difference([6, 3, 4, 1, 5]), [(1, 3), (3, 5), (4, 6)])
test.assert_equals(twos_difference([3, 1, 6, 4]), [(1, 3), (4, 6)])
test.assert_equals(twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]), [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])
test.assert_equals(twos_difference([1, 4, 7, 10]), [])
test.assert_equals(twos_difference([]), [])