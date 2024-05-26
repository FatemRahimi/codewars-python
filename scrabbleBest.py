# DESCRIPTION:
# You're playing to scrabble. But counting points is hard.

# You decide to create a little script to calculate the best possible value.

# The function takes two arguments :

# `points` : an array of integer representing for each letters from A to Z the points that it pays
# `words` : an array of strings, uppercase

# You must return the index of the shortest word which realize the highest score.
# If the length and the score are the same for two elements, return the index of the first one.


from string import ascii_uppercase as uppercase

def get_best_word(points, words):
    points = dict(zip(uppercase, points))
    
    score = lambda word: sum(points[c] for c in word)
    
    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])