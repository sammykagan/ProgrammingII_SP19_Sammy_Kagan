'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''

#1.  (6pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.
dictionary_list = []
file = open('dictionary.txt', 'r')
with open('dictionary.txt') as Samé:
    dictionary_list = [x.strip() for x in Samé]

longest_word = ""
longest_word_index = 0
longest_word_length = 0

for i in range(len(dictionary_list)):
    if len(dictionary_list[i]) >= longest_word_length:
        longest_word_length = len(dictionary_list[i])
        longest_word = dictionary_list[i]
        longest_word_index = i
print("\nLongest word is", longest_word)
print("Longest word index is", longest_word_index)
print("Longest word length is", longest_word_length)
file.close()


#2.  (8pts)  Write code which finds
# The total word count AND average word length
# in "AliceInWonderLand.txt"
import re
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
# This function takes in a line of text and returns
# a list of words in the line.


alice_list = []
words = []
alice_words = []

file = open('AliceInWonderLand.txt', 'r')
with open('AliceInWonderLand.txt') as Sam:
    alice_list = [x.strip() for x in Sam]

for i in range(len(alice_list)):
    words = split_line(alice_list[i])
    for word in words:
        alice_words.append(word)
word_count = len(alice_words)
total_letters = 0

for i in range(len(alice_words)):
    total_letters += len(alice_words[i])

average_word_length = total_letters/word_count

print("\nWord count is", word_count)
print("Average word length is", round(average_word_length, 2))

# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (12pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?

#### OR #####

#3  (12pts)Find the most frequently occurring
# seven letter word in "AliceInWonderLand.txt"

seven_letter_words = []
from collections import Counter

for i in range(len(alice_words)):
    if len(alice_words[i]) == 7:
        seven_letter_words.append(alice_words[i])
c = Counter(seven_letter_words)
print("")
print (c.most_common(1))





# Challenge problem (for fun).  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.



