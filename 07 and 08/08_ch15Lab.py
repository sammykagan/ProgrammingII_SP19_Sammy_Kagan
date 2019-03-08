'''
Complete the chapter lab at http://programarcadegames.com/index.php?chapter=lab_spell_check
'''

import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


dictionary_list = []
file = open('dictionary.txt', 'r')
with open('dictionary.txt') as dictionary:
    dictionary_list = [x.strip() for x in dictionary]

file.close()

# awesome. we just used a random function from the lab to split up our stuff into individual lines,
# imported the dictionary, and made it into a list.
# then we closed the dictionary.

print("\n--- LINEAR SEARCH ---")


import time
now0 = time.time()


file = open('AliceInWonderLand200.txt', 'r')
line_number = 0

in_dict = False
non_dict = []

for line in file:
    line_number += 1
    line_text = line.strip().upper()
    words = split_line(line_text)
    for word in words:
        key = word

        i = 0
        while i < len(dictionary_list) and dictionary_list[i] != key:
            i += 1

        if i < len(dictionary_list):
            dictionary_list=dictionary_list
        else:
            #non_dict.append([word, line_number])
            print(word, "is not in the dictionary, it is at line", line_number)
now = time.time() - now0

file.close()

file = open('AliceInWonderLand200.txt', 'r')
start = time.time()



line_number = 0

print("\n\n--- BINARY SEARCH ---")

for line in file:
    line_number += 1
    line_text = line.strip().upper()
    words = split_line(line_text)

    for word in words:

       minn = 0
       maxx = len(dictionary_list) - 1
       real_word = False
       key = word.upper()

       while minn <= maxx and not real_word:
           avg = (minn + maxx) // 2

           if dictionary_list[avg] < key:
               minn = avg + 1

           elif dictionary_list[avg] > key:
               maxx = avg - 1

           else:
               real_word = True

       if not real_word:
           print(key, "is not in the dictionary, it is at line", line_number)

end = time.time() - start
print("\nThe linear search took", round(now,2), "seconds.")
print("The binary search took", round(end,2), "seconds.")
timer = now/end
print("\nThe binary search was", round(timer,2), "times faster than the linear search.")
