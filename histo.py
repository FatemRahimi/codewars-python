# You will be given an array of non-negative integers and positive integer bin width.

# Your task is to create the Histogram method that will return histogram data corresponding to the input array. The histogram data is an array that stores under index i the count of numbers that belong to bin i. The first bin always starts with zero.

# On empty input you should return empty output.

# Examples:

# For input data [1, 1, 0, 1, 3, 2, 6] and binWidth=1 the result will be [1, 3, 1, 1, 0, 0, 1] as the data contains single element "0", 3 elements "1" etc.
# For the same data and binWidth=2 the result will be [4, 2, 0, 1]
# For input data [7] and binWidth=1 the result will be [0, 0, 0, 0, 0, 0, 0, 1]

def histogram(lst, w):
    lst = [n // w for n in lst]
    m = max(lst, default=-1) + 1
    return [lst.count(n) for n in range(m)]


test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 1), [1, 3, 1, 1, 0, 0, 1])
test.assert_equals(histogram([1, 1, 0, 1, 3, 2, 6], 2), [4, 2, 0, 1])
test.assert_equals(histogram([], 1), [])
test.assert_equals(histogram([8], 1), [0, 0, 0, 0, 0, 0, 0, 0, 1])