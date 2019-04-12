# SCRAPING LAB 
# (20pts)
# Below is a link to a 10-day weather forecast at weather.com
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days by grabbing each of the following:
# Day, date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (10pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:  
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.

# Note: Although it is possible to pull a description of the weather which includes much of this data, that is not the intent.
# However, if you can do it and add the additional info, that works for me.

# MY SOLE REMAINING ISSUE
# On the first day, The Weather Channel seems to have taken out the value for a high temp. That is, the
# high reads as "--/36" which messes with my program because the program splices at the "°" sign. Was today weird, or do
# they always do this? Is it really so important that I go off and deal with it separately? I say no...

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/USIL0225:1:US"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

# DAYS
day = soup.findAll(class_="date-time")
day_list = []
for j in day:
    day_list.append(j.text)
#print(day_list)


# DATES
date = soup.findAll(class_="day-detail clearfix")
date_list = []
for j in date:
    date_list.append(j.text)
#print(date_list)

# DESCRIPTIONS
description = soup.findAll(class_="description")
desc_list = []
for j in description:
    desc_list.append(j.text)
desc_list.pop(0)
#print(desc_list)

# HIGHS AND LOWS
temperature = soup.findAll(class_="temp")
temp_list = []
for j in temperature:
    temp_list.append(j.text)
temp_list.pop(0)
#print(temp_list)

#Build a list where the 'high' value and the 'low' value are separate items
temp_list2 = []
for k in temp_list:
    temp_list2.append(k.split('°'))
#print(temp_list2)

# GET RID OF THAT BLASTED BLANK VALUE IN THE 2 SLOT
# in retrospect, this was completely unnecessary
temp_list3 = []
for i in range(15):
    temp_list3.append([])

for i in range(len(temp_list2)):
    temp_list3[i].append(temp_list2[i][0])
    temp_list3[i].append(temp_list2[i][1])
#print(temp_list3)

# PRECIPITATION
precipitation = soup.findAll(class_="precip")
precip_list = []
for j in precipitation:
    precip_list.append(j.text)
precip_list.pop(0)
#print(precip_list)

# WIND
wind = soup.findAll(class_="wind")
wind_list = []
for j in wind:
    wind_list.append(j.text)
wind_list.pop(0)
#print(wind_list)

wind_list2 = []
for k in wind_list:
    wind_list2.append(k.split(' '))
#print(wind_list2)

# HUMIDITY
humidity = soup.findAll(class_="humidity")
humid_list = []
for j in humidity:
    humid_list.append(j.text)
humid_list.pop(0)
#print(humid_list)


for i in range(10):
    print("\n" + day_list[i] + ", " + date_list[i] + " will be " + desc_list[i].lower() + " with a high of " +
          str(temp_list3[i][0]) + "° and a low of " + temp_list3[i][1] + "° as humidity sits at " + humid_list[i] +
          ". Winds will come from the " + wind_list2[i][0] + " at " + wind_list2[i][1] + " mph and there is a " +
          precip_list[i] + " chance of rain.")





