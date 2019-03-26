# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s


#1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
#2  Plot bus usage for the same years as a second line on your graph. (5pts)
#3  Plot bus and rail usage together on a third line on your graph. (5pts)
#4  Add a title and label your axes. (5pts)
#5  Add a legend to show data represented by each of the three lines. (5pts)
#6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)

import matplotlib.pyplot as plt
import random
import csv
import matplotlib.ticker as tkr

with open("/Users/sammykagan/PycharmProjects/Programming2_SP19/.idea/CTA Ridership/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f) # makes a reader object to pull in the data
    data = list(reader) # cast the reader as a list

print(data)
header = data.pop(0)

year = [int(x[0]) for x in data[20:]]
rail_usage = [int(x[3]) for x in data[20:]]
bus_usage = [int(x[1]) for x in data[20:]]

combined_usage = []
for i in range(len(bus_usage)):
    total = rail_usage[i] + bus_usage[i]
    combined_usage.append(total)
print(combined_usage)

print(year)
print(rail_usage)

fig = plt.figure(1, tight_layout = True)
plt.plot(year, combined_usage, label = "Combined")
plt.plot(year, bus_usage, label = "Bus")
plt.plot(year, rail_usage, label = "Rail")

axis = fig.gca()
y_axis = axis.get_yaxis()
axis.yaxis.set_major_formatter(tkr.FuncFormatter(lambda x, p: "{:,}".format(x)))


plt.xlabel("Year")
plt.ylabel("Total Riders")
plt.title("Chicago Public Transportation Rail Ridership")
plt.legend()
plt.show()

#Explain the Trends:
#1 -- Bus ridership is on the decline as a consequence of the proliferation of affordable ridesharing services
#2 -- Overall ridership is on the decline as a consequence of the decline in Chicago's population

