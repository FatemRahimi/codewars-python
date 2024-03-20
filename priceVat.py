# Write a function that calculates the original product price, without VAT.

# Example
# If a product price is 200.00 and VAT is 15%, then the final product price (with VAT) is: 200.00 + 15% = 230.00

# Thus, if your function receives 230.00 as input, it should return 200.00

# Notes:

# VAT is always 15% for the purposes of this Kata.
# Round the result to 2 decimal places.
# If null value given then return -1
# MATHEMATICSFUNDAMENTALS
def excluding_vat_price(price):
    try: return round(price/1.15, 2)
    except: return -1
    


    # test
     import codewars_test as test
try:
    from solution import excluding_vat_price
except:
    from solution import excludingVatPrice as excluding_vat_price

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_approx_equals(excluding_vat_price(230.00), 200.00, margin=1e-2)
        test.assert_approx_equals(excluding_vat_price(123), 106.96, margin=1e-2)
        test.assert_approx_equals(excluding_vat_price(777), 675.65, margin=1e-2)
        test.assert_approx_equals(excluding_vat_price(460.00), 400.00, margin=1e-2)
        test.assert_approx_equals(excluding_vat_price(None), -1, margin=1e-2)