'''
Scenario:
A program that reads a sequence of numbers and counts how many numbers are even and how many are odd. The program terminates when zero is entered.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 202

Test Data:

Enter a number or type 0 to stop: 10
Enter a number or type 0 to stop: 20
Enter a number or type 0 to stop: 11
Enter a number or type 0 to stop: 11
Enter a number or type 0 to stop: 22
Enter a number or type 0 to stop: 20
Enter a number or type 0 to stop: 0
Odd numbers count: 2
Even numbers count: 4

'''

odd_numbers = 0
even_numbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)