# Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to remove the longest prefix of elements such that the predicate is true for each element. We'll call this the dropWhile function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence.

# def isEven(num):
#   return num % 2 == 0

# arr = [2,4,6,8,1,2,5,4,3,2]

# dropWhile(arr, isEven) == [1,2,5,4,3,2] # True
from itertools import dropwhile

def drop_while(arr, pred):
    return list(dropwhile(pred, arr))


from solution import drop_while
import codewars_test as test

@test.it("Basic tests")
def basic_tests():
    
    is_even=lambda n: not n%2
    is_odd=lambda n: n%2
    
    test.assert_equals(drop_while([2,6,4,10,1,5,4,3], is_even),[1,5,4,3])
    test.assert_equals(drop_while([2,100,1000,10000,10000,5,3,4,6], is_even),[5,3,4,6])
    test.assert_equals(drop_while([998,996,12,-1000,200,0,1,1,1], is_even),[1,1,1])
    test.assert_equals(drop_while([1,4,2,3,5,4,5,6,7], is_even),[1,4,2,3,5,4,5,6,7])
    test.assert_equals(drop_while([2,4,10,100,64,78,92], is_even),[])
    test.assert_equals(drop_while([1,2,3,4,5], is_odd),[2,3,4,5])
    test.assert_equals(drop_while([1,5,111,1111,1111,2,4,6,4,5], is_odd),[2,4,6,4,5])
    test.assert_equals(drop_while([-1,-5,127,86,902,2,1], is_odd),[86,902,2,1])
    test.assert_equals(drop_while([2,1,2,4,3,5,4,6,7,8,9,0], is_odd),[2,1,2,4,3,5,4,6,7,8,9,0])
    test.assert_equals(drop_while([1,3,5,7,9,111], is_odd),[])