# Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

# When positives and positives interact, they remain positive.
# When negatives and negatives interact, they remain negative.
# But when negatives and positives interact, they become neutral, and are shown as the number 0.
# Worked Example
# ("+-+", "+--") ➞ "+-0"
# # Compare the first characters of each string, then the next in turn.
# # "+" against a "+" returns another "+".
# # "-" against a "-" returns another "-".
# # "+" against a "-" returns "0".
# # Return the string of characters.
# Examples
# ("--++--", "++--++") ➞ "000000"

# ("-+-+-+", "-+-+-+") ➞ "-+-+-+"

# ("-++-", "-+-+") ➞ "-+00"
def neutralise(s1, s2):
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result += "0"
    return result

# test
import codewars_test as test
from solution import neutralise

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(neutralise("--++--", "++--++"), "000000")
        test.assert_equals(neutralise("-+-+-+", "-+-+-+"), "-+-+-+")
        test.assert_equals(neutralise("-++-", "-+-+"), "-+00")
        test.assert_equals(neutralise("--++", "++++"), "00++")
        test.assert_equals(neutralise("+++--+---", "++----++-"), "++0--000-")
        test.assert_equals(neutralise("-----", "-----"), "-----")
        test.assert_equals(neutralise("-+", "++"), "0+")
        test.assert_equals(neutralise("--", "-+"), "-0")
        test.assert_equals(neutralise("-++", "+--"), "000")
        test.assert_equals(neutralise("++-++--++-", "-+++-++-++"), "0+0+0000+0")
        test.assert_equals(neutralise("-++-+-++-", "+-++++---"), "00+0+000-")
        test.assert_equals(neutralise("---++-+--", "-+++--++-"), "-00+0-+0-")
        test.assert_equals(neutralise("+-----+++-", "--+-+-++--"), "0-0-0-++0-")
        test.assert_equals(neutralise("+-----+-", "---++-++"), "0--00-+0")
        test.assert_equals(neutralise("-+--+-+---", "-+--+-+-+-"), "-+--+-+-0-")
        test.assert_equals(neutralise("+-+", "-++"), "00+")
        test.assert_equals(neutralise("-++", "-+-"), "-+0")
        test.assert_equals(neutralise("---+", "-+++"), "-00+")
        test.assert_equals(neutralise("+--", "+--"), "+--")
        test.assert_equals(neutralise("--+++-+-", "+++++---"), "00+++-0-")