'''
Scenario:
A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever!

The task is to help the magician complete the code in such a way so that the code:

1.will ask the user to enter an integer number;
2.will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."
The magician is counting on you! Don't disappoint him.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 202

Test Data:

Enter number: 22
Enter number: 88
Enter number: 777

+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
'''

secret_number = 777

flag = True

while flag:
    number = int(input("Enter number: "))
    if number == secret_number:
        flag=False
        break

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")