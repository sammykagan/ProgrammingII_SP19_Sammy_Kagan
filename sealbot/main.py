import csv
import tweepy as tw
import datetime
import time
import random

data = []
run = True

with open("positive_adjectives_final.csv") as f:
    for row in f:
        row = "".join(row)
        data.append(row)

data = [x.rstrip('\n') for x in data]
random.shuffle(data)

currentDT = datetime.datetime.now()

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
api.update_status("Hello!")



hour = ""
suffix = ""
chicago_time = ""
minute = ""
while run is True:
    for i in range(len(data)):
        chicago_time = currentDT.hour - 5
        if chicago_time > 12:
            hour = chicago_time - 12
        else:
            hour = chicago_time
        if chicago_time > 11:
            suffix = "p.m."
        else:
            suffix = "a.m."
        if currentDT.minute < 10:
            minute = "0" + str(currentDT.minute)
        else:
            minute = currentDT.minute
        print("Hey Seal! It's " + str(hour) + ":" + str(minute) + " " + str(suffix) + " and I just want to say that you're " + str(
            data[i]).lower() + ("."))
        time.sleep(random.randrange(300, 1200))

