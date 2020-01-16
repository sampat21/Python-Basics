"""
Scenario:
VOWEL EATER: A very simply mini console game where the user is asked to input a list of words and in return receives a new list with
the same words but without the vowels.

Author: Supriya Jadhav

Version: 1.0

Date Created: Jan 16, 2020

Test data:
Sample input: My name is Supriya. I am checking the accuracy of vowel eater program. Have fun!

Expected output:
My nm s Spry. I m chckng th ccrcy f vwl tr prgrm. Hv fn!

"""

import sys

# Return a list of words without vowels.
def eat_vowels(words):
  leftovers = []
  if words != ['']:
    for word in words:
      leftover = ""
      for letter in word:
        if letter not in "aeiou":
          leftover += letter
      # Uppercase the first letter of each word.
      leftover = (leftover[0].upper() + leftover[1:])
      leftovers.append(leftover)
  return leftovers

# Main function.
def play():

  while True:
    try:
      words = input("Hi! I'm hungry and want to eat some delicious wovels. "
                    "Enter some words separated by a comma to feed me.\n > ").split(', ')
    except ValueError:
      print("Hey! Those are not even words! Yack!")
    else:
      eat_vowels(words)
      print("Yummy! This is what you got left with:")
      print(", ".join(eat_vowels(words)))
      # Prompt the user wether to play again or not.
      play_again = ""
      while play_again != "y" or play_again != "n":
        play_again = input("Play again? Y/n ").lower()
        if play_again == "n":
          sys.exit()
        else:
          break

# Run the game.
play()