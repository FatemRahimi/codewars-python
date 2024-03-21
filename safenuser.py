

ef html_special_chars(data):
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
