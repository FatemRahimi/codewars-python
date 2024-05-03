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

