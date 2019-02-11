'''
Make a text based version of hangman (25pts)
Use the sample run as an example.  Try to make it as close as possible to the example. (or better)
'''

# PSEUDOCODE
# make a word list for your game
# grab a random word from your list and store it as a variable
# display the hangman
# display the used letters
# display the length of the word to the user using blank spaces
# prompt the user to guess a letter
# if the guess is correct increment correct_guesses by 1
# if the guess is incorrect increment incorrect_guesses by 1 and draw the next part of the hangman
# don't allow the user to select the same letter twice
# if the incorrect_guesses is greater than 6, tell the user they lost and exit the program
# if correct_guesses is equal to the length of the word, tell the user they won
# ask if they want to play again


# Feel free to use this list of ascii art for your game

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

#Create the list of words and establish the word the player is trying to solve
word_list = ["Lindsay", "FWPMUN", "Weekly", "Avani", "Colonel", "Klobuchar"]
word = (word_list[random.randrange(0, len(word_list))])
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
available_letters = alphabet

#Let's begin motherheckers
print("\nWelcome to HANGMAN!\n")
print("Here's your current board")
print(HANGMANPICS[0])
print("Here are the letters available to guess")
print (available_letters)
print("\nHere's the word you're guessing")
for i in range (len(word)):
    print ("__", end = " ")
print ("\nIt's " + str(len(word)) + " letters long!")

guess = input("\nGuess a letter!\n")
available_letters.pop(available_letters.index(guess.upper()))

if guess in word:
    position = word.index(guess)
    for i in range (len(position)):
        print("__", end = " ")
    print(guess)
    for i in range (len(word - position))


