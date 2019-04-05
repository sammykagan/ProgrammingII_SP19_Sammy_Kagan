# SCRAPING PROBLEM (12pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

from bs4 import BeautifulSoup
import requests

url = "https://twitter.com/KylePlantEmoji"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

tweet = soup.findAll(class_="tweet-text")

tweet_list = []

for j in tweet:
    tweet_list.append(j.text)

print("\n\nTweets from", url)

for i in range(5):
    print("\n---------------------------------------\n")
    print(tweet_list[i])
print("\n--------------------------------------")