'''
Scenario:
The program will ask the user to enter a word. Convert the word entered by the user to upper case. Use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word. Print the uneaten letters to the screen, each one of them on a separate line.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 2020

Test Data:

Sample input: Gregory
Expected output:
G
R
G
R
Y
'''


userWord = input("Enter a word : ")
userWord = userWord.upper()

for letter in userWord:
    # Complete the body of the for loop.
    if letter not in 'AEIOU':
        print(letter)
