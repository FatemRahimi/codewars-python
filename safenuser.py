# Safen User Input Part I - htmlspecialchars
# You are a(n) novice/average/experienced/professional/world-famous Web Developer (choose one) who owns a(n) simple/clean/slick/beautiful/complicated/professional/business website (choose one or more) which contains form fields so visitors can send emails or leave a comment on your website with ease. However, with ease comes danger. Every now and then, a hacker visits your website and attempts to compromise it through the use of XSS (Cross Site Scripting). This is done by injecting script tags into the website through form fields which may contain malicious code (e.g. a redirection to a malicious website that steals personal information).

# Mission
# Your mission is to implement a function that converts the following potentially harmful characters:

# < --> &lt;
# > --> &gt;
# " --> &quot;
# & --> &amp;
# Good luck :D

def html_special_chars(data):
    specials = {
        '<': '&lt;',
        '>': '&gt;',
        '\"': '&quot;',
        '&': '&amp;',
    }       
    return ''.join(specials.get(char, char) for char in data)


import codewars_test as test
from solution import html_special_chars
import string
from random import randint, choices
# tested
@test.describe("Example")
def test_group():
    @test.it("Testing Simple Examples")
    def simple_test_cases():
        test.assert_equals(html_special_chars("<h2>Hello World</h2>"), "&lt;h2&gt;Hello World&lt;/h2&gt;")
        test.assert_equals(html_special_chars("Hello, how would you & I fare?"), "Hello, how would you &amp; I fare?")
        test.assert_equals(html_special_chars('How was "The Matrix"?  Did you like it?'), 'How was &quot;The Matrix&quot;?  Did you like it?')
        test.assert_equals(html_special_chars("<script>alert('Website Hacked!');</script>"), "&lt;script&gt;alert('Website Hacked!');&lt;/script&gt;")
