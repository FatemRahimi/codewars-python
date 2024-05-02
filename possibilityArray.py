# ""

def is_all_possibilities(arr):
    if arr == []:
        return False
    arr.sort()
    for i in range(len(arr)):
        if arr[i] != i:
            return False
    return True