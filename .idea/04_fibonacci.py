import math
import random

# Let's go motherduckers

prev_two = 0
prev = 1

print("1")
for i in range(1000):
    number = prev_two + prev
    prev_two = prev
    prev = number
    print (number)


