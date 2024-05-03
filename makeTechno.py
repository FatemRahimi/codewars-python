# This kata is a very basic introduction to compression.

# Your task is to make a program which takes in a sentence and returns a string which shows the unique position of each word in the sentence. If a word appears more than once in the sentence, your string should return the position of the first occurrence of the word.

# Unique position in this case means the position of the word excluding repeated words. Capitalisation of words should be accounted for: 'BEE' should be considered the same as 'bee'. The sentences include no punctuation.

# Example
# "man hello man"

# becomes

# "010"

# Example
# "THE ONE BUMBLE BEE one bumble the bee"

# becomes

# "01231203"

# Example
# "Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"

# becomes

# "01234567802856734"

def compress(sentence):
    ref = []
    for i in sentence.lower().split():
        if i not in ref:
            ref.append(i)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])


import codewars_test as test
from solution import compress

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(compress("The bumble bee"), "012")
        test.assert_equals(compress("SILLY LITTLE BOYS silly little boys"), "012012")
        test.assert_equals(compress("Ask not what your COUNTRY can do for you ASK WHAT YOU CAN DO FOR YOUR country"), "01234567802856734")
        test.assert_equals(compress("The number 0 is such a strange number Strangely it has zero meaning"), "012345617891011")