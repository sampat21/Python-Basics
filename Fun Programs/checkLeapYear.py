'''
Scenario:
As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 202

Test Data:

Sample input: 2000
Expected output: Leap year

Sample input: 1999
Expected output: Common Year

Sample input: 2017
Expected output: Common year

'''

year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year, " is a leap year")
       else:
           print(year, " is a leap year")
   else:
       print(year, " is a leap year")
else:
   print("{0} is not a leap year".format(year))