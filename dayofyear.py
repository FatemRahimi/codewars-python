# Work out what number day of the year it is.

# toDayOfYear([1, 1, 2000]) => 1
# The argument passed into the function is an array with the format [D, M, YYYY], e.g. [1, 2, 2000] for February 1st, 2000 or [22, 12, 1999] for December 22nd, 1999.

# Don't forget to check for whether it's a leap year! Three criteria must be taken into account to identify leap years:

# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
def to_day_of_year(date):
    
    days,months,year = date
    
    for month in range(months-1): 
        if month == 1:
            # checks if it is a leap year or not
            if (year % 4 == 0) and (year % 100 != 0):
                days += 29
            elif (year % 100 == 0) and (year % 400 == 0): 
                days += 29
            else: 
                days += 28
        else:
            if month == 3 or month == 5 or month == 8 or month == 10:  # months with 30days; april, june, september and november respectively
                days += 30
            else:
                days += 31
     
    return days
# tested
import codewars_test as test
from solution import to_day_of_year 

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(to_day_of_year([25, 12, 2017]), 359,);
        test.assert_equals(to_day_of_year([31, 10, 1991]), 304);
        test.assert_equals(to_day_of_year([1, 5, 3000]), 121);
        test.assert_equals(to_day_of_year([14, 3, 1066]), 73);
        test.assert_equals(to_day_of_year([5, 11, 1604]), 310);

        test.assert_equals(to_day_of_year([31, 12, 2000]), 366);
        test.assert_equals(to_day_of_year([31, 12, 2001]), 365);
        test.assert_equals(to_day_of_year([31, 12, 2004]), 366);
        test.assert_equals(to_day_of_year([31, 12, 2100]), 365);