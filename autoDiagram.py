# (If this kata isn't hard enough, see Autodigigrams – Part 2.)

# In this kata, you will write a program that checks whether a given list of integers is an autodigigram.

# The idea is inspired by autograms, which are self-referential sentences that correctly state how often each letter occurs in their words. For example:

# This autogram contains five a's, one b, two c's, two d's, twenty-six e's, six f's, two g's, four h's, thirteen i's, one j, one k, one l, two m's, twenty-one n's, sixteen o's, one p, one q, five r's, twenty-seven s's, twenty t's, three u's, six v's, nine w's, five x's, five y's, and one z.

# Instead of sentences, we'll look at lists of numbers. If a list of integers correctly enumerates how often each digit occurs in it — i.e. the value at index d is equal to the total occurrence count of digit d — we'll call it an autodigigram.

# Your task is to write a program that checks whether a given list of integers is an autodigigram when its numbers are represented in a given base and width (possibly with leading zeros).

# Examples:

# [6, 2, 1, 0, 0, 0, 1, 0, 0, 0] is an autodigigram of decimal one-digit numbers because it contains six 0's, two 1's, one 2, one 6, and zero of the other digits.
# [1B, 03, 00, 01, 00, 00, 00, 00, 00, 00, 00, 01, 00, 00, 00, 00] is an autodigigram of hexadecimal two-digit numbers that contains twenty-seven (1B in hexadecimal) 0's, three 1's, one 3, one B, and zero of the other hexadecimal digits.
# [01000, 00010] is an autodigigram of binary five-digit numbers that contains eight 0's and two 1's.
# [10, 02, 01] is an autodigigram of ternary two-digit numbers that contains three 0's, two 1's, and one 2.
# You can assume (without having to check) that the input will satisfy the following conditions:

# base ranges from 2 to 36
# width ranges from 1 to 30
# list has the correct length, i.e. base elements
# list contains only non-negative numbers
# no number in list exceeds width when represented in base