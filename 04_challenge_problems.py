# PROBLEM 1 (Fibonacci)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

import math
import random

# Let's go motherduckers

prev_two = 0
prev = 1
stop = False
number = prev + prev_two

while stop == False:
    print(number)
    number = prev_two + prev
    if number > 1000:
        stop = True
    prev_two = prev
    prev = number


# PROBLEM 2 (Dice Sequence)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.

die_1 = random.randrange(1, 7)
die_2 = random.randrange(1, 7)
die_3 = random.randrange(1, 7)
die_4 = random.randrange(1, 7)
die_5 = random.randrange(1, 7)
trials = 100000
success = 0
failure = 0
success_pct = 0

for i in range(trials):
    die_1 = random.randrange(1, 7)
    die_2 = random.randrange(1, 7)
    die_3 = random.randrange(1, 7)
    die_4 = random.randrange(1, 7)
    die_5 = random.randrange(1, 7)
    if die_5 >= die_4 and die_4 >= die_3 and die_3 >= die_2 and die_2 >= die_1:
        success += 1
    else:
        failure += 1
success_pct = (success/trials) * 100
print("")
print(str(success) + " successes, " + str(failure) + " failures. That's a success percentage of " + str(success_pct) +"%")

# PROBLEM 3 (Number Puzzler)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 
