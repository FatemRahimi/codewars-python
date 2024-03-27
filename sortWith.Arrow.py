# Yet another staple for the functional programmer. You have a sequence of values and some predicate for those values. You want to remove the longest prefix of elements such that the predicate is true for each element. We'll call this the dropWhile function. It accepts two arguments. The first is the sequence of values, and the second is the predicate function. The function does not change the value of the original sequence.

# def isEven(num):
#   return num % 2 == 0

# arr = [2,4,6,8,1,2,5,4,3,2]

# dropWhile(arr, isEven) == [1,2,5,4,3,2] # True

def drop_while(arr, pred):
    pass #your code here