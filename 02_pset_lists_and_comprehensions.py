#LISTS (29PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.

import random
print("\n")

# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)

print("PROBLEM 1\n")


# A
my_nums_0 = [ ]
for i in range(1,101):
    my_nums_0.append(i)
print("a) Make a list of numbers from 1 to 100")
print (my_nums_0)
print("")

# B
my_nums_1 = [ ]
for i in range (20, 41, 2):
    my_nums_1.append(i)
print("b) Make a list of even numbers from 20 to 40")
print (my_nums_1)
print("")

# C
my_nums_2 = [ ]
for i in range (1, 101):
    j = i ** 2
    my_nums_2.append(j)
print("c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)")
print (my_nums_2)
print("\n")



#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

("INSERT YOUR QUESTION HERE") # to give the illusion that the 8-ball is responding to user input.
# you know. like deception.

print("PROBLEM 2\n")
answer_num = random.randrange(20)
print("8-ball says...")
print (answer_list[answer_num])


# PROBLEM 3 (Shuffle - 8pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order. Print the random deck. 
# Then deal yourself a hand of 5 cards off the top.  Print the hand.  Print the remaining deck.

print("\n\nPROBLEM 3\n")
# Create the deck
my_cards = [ ]
my_suits = ["Heart", "Diamond", "Club", "Spade"]
my_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for value in range (13):
    for suit in range(4):
        my_cards.append([my_values[value], my_suits[suit]])

# Shuffle the deck
print("Print the random deck.")
random.shuffle(my_cards)
print(my_cards)
print("")

# Deal those cards and deal them good
my_hand = []
for i in range(5):
    my_hand.append(my_cards[i])
print("Then deal yourself a hand of 5 cards off the top.  Print the hand.")
print(my_hand)
print("\nPrint the remaining deck.")
print(my_cards[5:])



# PROBLEM 4 (Illinois Pick 4 - 10pts)
# Lotteries are known to give awful odds of winning, and incredibly low expected returns on your invevestment.
# You will buy 10000 Illinois Pick 4 tickets in a simulation.
# Make a 2d lists of your picks.  Each number is a random 0 to 9.
# After you have made a list of 10000 lists (each 4 long), you will draw the official numbers
# After drawing the official numbers, you will go back through your list and check to see how many wins you got.
# The numbers must be an exact match in the exact position.
# Each ticket is $1.  If you win, you get $5000.  Simulate spending $10,000 on Pick 4 tickets, and see your return.
print("\n\nPROBLEM 4\n")
my_tix = []
for i in range(10000):
    for j in range(4):
        my_tix.append([random.randrange(0,10), random.randrange(0,10), random.randrange(0,10), random.randrange(0,10)])

winning_numbers = [random.randrange(0,10), random.randrange(0,10), random.randrange(0,10), random.randrange(0,10)]
print("The winning numbers are " + str(winning_numbers))
num_0 = winning_numbers[0]
num_1 = winning_numbers[1]
num_2 = winning_numbers[2]
num_3 = winning_numbers[3]

winning_tix = 0
my_cash = 0
plural = True

for i in range(10000):
    my_cash -= 1
    if my_tix[i][0] == num_0 and my_tix[i][1] == num_1 and my_tix[i][2] == num_2 and my_tix[i][3] == num_3:
        my_cash += 5000
        winning_tix += 1
message = ""
if winning_tix >= 3:
    message = "! Congratulations!"
else:
    if winning_tix == 2:
        message = ". I hope you had fun!"

    else:
        message = ". That's the danger of gambling."

        if winning_tix == 1:
            plural = False

time = "times"

if plural is True:
    time = "times"

else:
    time = "time"


print("\nYou won " + str(winning_tix) + " " + str(time) + " and earned $" + str(my_cash) + str(message))




