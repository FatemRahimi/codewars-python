# Among the ruins of an ancient city a group of archaeologists found a mysterious function with lots of HOLES in it called getNum(n) (or get_num(n) in ruby, python, or r). They tried to call it with some arguments. And finally they got this journal:

# getNum(300) #-> returns 2
# getNum(90783) #-> returns 4
# getNum(123321) #-> returns 0
# getNum(89282350306) #-> returns 8
# getNum(3479283469) #-> returns 5
# The archaeologists were totally stuck with this challenge. They were all in desperation but then.... came YOU the SUPER-AWESOME programmer. Will you be able to understand the mystery of this function and rewrite it?

def get_num(n):
    sum = 0
    for i in str(n):
        sum += int(i)//4 if i=='8' else 0 if i not in '069' else 1
    return sum

# tested
import codewars_test as test
from solution import get_num

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_num(300), 2, "Wrong output!")
        test.assert_equals(get_num(90783), 4, "Wrong output!")
        test.assert_equals(get_num(123321), 0, "Wrong output!")
        test.assert_equals(get_num(89282350306), 8, "Wrong output!")
        test.assert_equals(get_num(3479283469), 5, "Wrong output!")