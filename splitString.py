# You have two arguments: string - a string of random letters(only lowercase) and array - an array of strings(feelings). Your task is to return how many specific feelings are in the array.

# For example:

# string -> 'yliausoenvjw'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '3 feelings.' // 'awe', 'joy', 'love'


# string -> 'griefgriefgrief'
# array -> ['anger', 'awe', 'joy', 'love', 'grief']
# output -> '1 feeling.' // 'grief'


# string -> 'abcdkasdfvkadf'
# array -> ['desire', 'joy', 'shame', 'longing', 'fear']
# output -> '0 feelings.'
# If the feeling can be formed once - plus one to the answer.

# If the feeling can be formed several times from different letters - plus one to the answer.

# Eeach letter in string participates in the formation of all feelings. 'angerw' -> 2 feelings: 'anger' and 'awe'.


from collections import Counter

def countFeelings(letters, feelings):
    counter = Counter(letters)
    result = sum(not(Counter(feeling) - counter) for feeling in feelings)
    return "{} feeling{}.".format(result, "s" if result != 1 else "")


    import codewars_test as test
try: 
    from solution import countFeelings as count_feelings
except:
    from solution import count_feelings

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_feelings('longi', ['anger', 'awe', 'joy', 'longing', 'grief']), '0 feelings.');
        test.assert_equals(count_feelings('yliausoenvjw', ['anger', 'awe', 'joy', 'love', 'grief']), '3 feelings.');
        test.assert_equals(count_feelings('angerw', ['anger', 'awe', 'joy', 'love', 'grief']), '2 feelings.');
        test.assert_equals(count_feelings('griefgriefgrief', ['anger', 'awe', 'joy', 'love', 'grief']), '1 feeling.');
        test.assert_equals(count_feelings('abcdkasdfvkadf', ['desire', 'joy', 'shame', 'longing', 'fear']), '0 feelings.');