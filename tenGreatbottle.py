# Ten green bottles hanging on the wall,
# Ten green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There'll be nine green bottles hanging on the wall.

# Nine green bottles hanging on the wall,
# Nine green bottles hanging on the wall,
# And if one green bottle should accidentally fall,
# There'll be eight green bottles hanging on the wall. 

# Eight green bottles hanging on the wall...
# Seven green bottles hanging on the wall...
# ...

# One green bottle hanging on the wall,
# One green bottle hanging on the wall,
# If that one green bottle should accidentally fall,
# There'll be no green bottles hanging on the wall.
# Task
# Write some amazing code to reproduce the above lyrics starting from n green bottles!

# parameter n is 1 to 10
# newline terminates every line (including the last)
# don't forget the blank lines between the verses

def ten_green_bottles(n):
    dict1 = {1:'One green bottle',2:'Two green bottles',3:'Three green bottles',4:'Four green bottles',5:'Five green bottles',6:'Six green bottles',7:'Seven green bottles',8:'Eight green bottles',9:'Nine green bottles',10:'Ten green bottles'}
    list1 = []
    while n != 0:
        if n == 1:
            str1 = "One green bottle hanging on the wall,\nOne green bottle hanging on the wall,\nIf that one green bottle should accidentally fall,\nThere'll be no green bottles hanging on the wall.\n"
        else:
            str1 = f"{dict1[n]} hanging on the wall,\n{dict1[n]} hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {dict1[n - 1].lower()} hanging on the wall.\n\n"
        n = n - 1
        list1.append(str1)
    return ''.join(list1)


def number_to_words(n):
    num_words = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"
    }
    return num_words[n]

def ten_green_bottles(n):
    verses = []
    for i in range(n, 0, -1):
        number = number_to_words(i)
        next_number = number_to_words(i - 1) if i > 1 else "no"
        if i > 1:
            verses.append(f"{number} green bottles hanging on the wall,")
            verses.append(f"{number} green bottles hanging on the wall,")
            verses.append("And if one green bottle should accidentally fall,")
            if i - 1 > 1:
                verses.append(f"There'll be {next_number.lower()} green bottles hanging on the wall.")
            else:
                verses.append(f"There'll be {next_number.lower()} green bottle hanging on the wall.")
        else:
            verses.append("One green bottle hanging on the wall,")
            verses.append("One green bottle hanging on the wall,")
            verses.append("If that one green bottle should accidentally fall,")
            verses.append("There'll be no green bottles hanging on the wall.")
        if i > 1:
            verses.append("")  # Blank line between verses
    return "\n".join(verses) + "\n"





import codewars_test as test
from solution import ten_green_bottles

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        expected = "Two green bottles hanging on the wall,\n"\
        "Two green bottles hanging on the wall,\n"\
        "And if one green bottle should accidentally fall,\n"\
        "There'll be one green bottle hanging on the wall.\n"\
        "\n"\
        "One green bottle hanging on the wall,\n"\
        "One green bottle hanging on the wall,\n"\
        "If that one green bottle should accidentally fall,\n"\
        "There'll be no green bottles hanging on the wall.\n"
        test.assert_equals(ten_green_bottles(2), expected)