# reate a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

# Worked Example
# 2520 ➞ 72

# # The first and last digits are 2 and 0.
# # 2 and 0 form 20.
# # The second digit is 5 and the second to last digit is 2.
# # 5 and 2 form 52.

# # 20 + 52 = 72
# Examples
# 121 ➞ 13
# # 11 + 2

# 1039 ➞ 22
# # 19 + 3

# 22225555 ➞ 100
# # 25 + 25 + 25 + 25
# Notes
# If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
# Any number which is zero-padded counts as a single digit (see example #2).

def closing_in_sum(n):
    n_str = str(n)

    left = 0 
    right = len(n_str) - 1

    total = 0

    while left <= right:
        left_number = n_str[left]
        right_number = n_str[right]

        if left_number == right_number and left == right:
            total += int(f"{right_number}")
        else:
            total += int(f"{left_number}{right_number}")

        left += 1
        right -= 1

    return total