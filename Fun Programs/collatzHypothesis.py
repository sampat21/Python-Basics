'''
Scenario:
In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
The hypothesis says that regardless of the initial value of c0, it will always go to 1.

This program reads one natural number and executes the above steps as long as c0 remains different from 1. It also counts the steps needed to achieve the goal and outputs all the intermediate values of c0, too.


Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 2020

Test Data:

Sample input: 16
Expected output:

8
4
2
1
steps = 4
'''

def printCollatz(num):
    steps = 0
    while num != 1:
        print(num, end = '\n')

        # If n is even
        if num % 2 == 0:
            num = int(num / 2)

        # If odd
        else:
            num = int(3 * num + 1)
        steps = steps+1

    # Print 1 at the end
    print(num)

    return steps

# Driver code
num = int(input("Enter number: "))
count = printCollatz(num)
print("Steps: ", count)