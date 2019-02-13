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
word_list = ["BIDEN", "SANDERS", "BOOKER", "GILLIBRAND", "KLOBUCHAR", "HARRIS", "DELANEY", "CASTRO", "BUTTIGIEG", "GABBARD", "WARREN", "BROWN", "HICKENLOOPER", "OROURKE", "KAGAN"]
word = (word_list[random.randrange(0, len(word_list))])
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
available_letters = alphabet
word_list = []
your_letters = []
#Let's begin motherheckers
print("\nWelcome to 2020 Democrat HANGMAN!\n")
print("\nEvery word in this game is the last name of a Democrat who has or is expected to run for the Presidential nomination")
print("Here's your current board")
print(HANGMANPICS[0])
print("Here are the letters available to guess")
print (available_letters)
print("\nHere's the word you're guessing")
for i in range (len(word)):
    word_list.append("_")
print(word_list)
print ("\nIt's " + str(len(word)) + " letters long!")

wrong = 0
good_guesses = 0
game_on = True
correct = False
right = False
letters_remaining = True

while game_on is True:
    correct = False
    guess = input("\nGuess a letter!\n").upper()


    if guess in your_letters:
        print("\nHey you already guessed that letter, idiot.\n")
        wrong -= 1
    else:
        if guess in word:
            correct = True
        your_letters.append(guess.upper())

    letters_remaining = False


    print("")

    for i in word:
        if i in your_letters:
            print(i + " ", end="")
        else:
            print("_ ", end="")
            letters_remaining = True

    if correct == False:
        wrong += 1
    else:
        wrong = wrong

    print(HANGMANPICS[wrong])

    print("\nHere are the letters you've guessed")
    print(your_letters)

    if wrong == 6:
        print("\nGame over, you lost!")
        print("\nThe word was " + str(word))
        game_on = False

    if letters_remaining == False:
        print("\nGame over, you won!")
        print("\nThe word was " + str(word))
        game_on = False


