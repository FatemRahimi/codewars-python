
# Python
# TRAINNEXT KATA
# Details
# Solutions
# Forks (2)
# Discourse (22)
# Collect|
# DESCRIPTION:
# Suppose a student can earn 100% on an exam by getting the answers all correct or all incorrect. Given a potentially incomplete answer key and the student's answers, write a function that determines whether or not a student can still score 100%. Incomplete questions are marked with an underscore, "_".

# ["A", "_", "C", "_", "B"]   # answer key
# ["A", "D", "C", "E", "B"]   # student's solution

# ➞ True

# # Possible for student to get all questions correct.

# ["B", "_", "B"]   # answer key
# ["B", "D", "C"]   # student's solution

# ➞ False

# # First question is correct but third is wrong, so not possible to score 100%.

# ["T", "_", "F", "F", "F"]   # answer key
# ["F", "F", "T", "T", "T"]   # student's solution

# ➞ True

# # Possible for student to get all questions incorrect.
# Examples

# (["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True

# (["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True

# (["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False

# (["B", "_"], ["C", "A"]) ➞ True

# (["B", "A"], ["C", "A"]) ➞ False

# (["B"], ["B"]) ➞ True

# (["_"], ["B"]) ➞ True


def possibly_perfect(solutions, answers):
    
    pass_ans = 0
    correct = 0
    
    for x,y in zip(solutions, answers):
        
        if x == '_':
            
            pass_ans += 1
            continue
            
        if x == y:
            
            correct += 1
            
    return correct == 0 or correct == (len(solutions) - pass_ans)