
# "Getting into the tech sector has been tough for me mainly because I didn’t know where to start. I didn’t study tech or computer stuff in school, so I felt like I was way behind everyone else who did. Plus, tech stuff can be expensive, like needing a good computer or paying for classes, and that was hard for me to afford.

# Also, where I live, there aren’t many people working in tech that I know of, so I didn’t have anyone to ask for advice or guidance. It kind of felt like trying to find my way in the dark without a map.

# I think the bootcamp will be a huge help for me. First, it’s like getting that map I was missing. It’s going to show me step by step what I need to learn and do to get into the tech industry. It’s also cool that the bootcamp seems to understand that not everyone comes from the same background or has the same resources, so it’s set up to help people like me get started.

# By learning the actual skills I need for a tech job, and getting to practice them, I’ll feel way more confident applying for jobs. And, the bootcamp has mentors and a community of people who are also learning or have already made it into tech, so I won’t feel so alone in this journey. It’s like finally finding a group of people who get what I’m going through and can help guide me along the way."

def counter():
    count = 0
    def function():
        nonlocal count
        count += 1
        return count
    return function


import codewars_test as test
from solution import counter

@test.describe("counter")
def test_group():
    @test.it("should return a function")
    def function():
        test.assert_equals(type(counter).__name__, 'function')
    @test.it("should return 1 when the returned function is invoked")
    def return_1():
        test.assert_equals(counter()(), 1)
    @test.it("should increment and return the number each time the function is invoked")
    def increment():
        counter_function = counter()
        test.assert_equals(counter_function(), 1)
        test.assert_equals(counter_function(), 2)
    @test.it("should have two different accumulators if two counters are created")
    def multi_accumulate():
        counter_one = counter()
        counter_two = counter()
        test.assert_equals(counter_one(), 1)
        test.assert_equals(counter_one(), 2)
        test.assert_equals(counter_two(), 1)
        test.assert_equals(counter_two(), 2)