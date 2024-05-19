# DESCRIPTION:
# You'll be given a string of characters as an input. Complete the function that returns a list of strings: (a) in the reverse order of the original string, and (b) with each successive string starting one character further in from the end of the original string.

# Assume the original string is at least 3 characters long. Try to do this using slices and avoid converting the string to a list.

# Examples
# '123'   ==>  ['321', '21', '1']
# 'abcde' ==>  ['edcba', 'dcba', 'cba', 'ba', 'a']

def reverse_slice(s):
    return [s[::-1][i:] for i in range(len(s))]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_slice('123'), ['321', '21', '1'])
        test.assert_equals(reverse_slice('abcde'), ['edcba', 'dcba', 'cba', 'ba', 'a'])