# Given a 2D array of some suspended blocks (represented as hastags), return another 2D array which shows the end result once gravity is switched on.

# Examples
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "#", "#", "-"]
# ]

# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "-", "-", "-"],
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "#", "#", "-"]
# ]

# switch_gravity([
#   ["-", "#", "#", "#", "#", "-"],
#   ["#", "-", "-", "#", "#", "-"],
#   ["-", "#", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "#", "-", "#", "#", "-"],
#   ["#", "#", "#", "#", "#", "-"]
# ]

def switch_gravity(a):
    r = len(a)  # amount of rows
    c = len(a[0])  # amount of cols
    j = 0
    while j <= c -1:
        k = 0
        while k < r - 1:  # use a buble sorting for each column
            i = 0
            while i < r - 1:
                if a[i][j] < a[i+1][j]:
                    a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
                i += 1
            k +=1
        j += 1
    return a