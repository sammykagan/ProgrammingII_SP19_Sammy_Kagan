# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50,000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:

- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
'''

import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

green_house_emmissions = []
building_square_footage = []
buildings = []
full_schools = []
intensity = []

for building in data:
    if building[6] == "K-12 School":
        full_schools.append(building)


for building in data:
    if building in full_schools:
        try:
            green_house = float(building[20])
            building_footage = float(building[7])
            name = building[2]
            ghg_strength = float(building[21])
            green_house_emmissions.append(green_house)
            building_square_footage.append(building_footage)
            buildings.append(name)
            intensity.append(ghg_strength)
            print(name)
            print(ghg_strength)
        except:
            print(building[2], "had incomplete data.")

#print(intensity)
#print(buildings)

intensity_list = [[buildings[x], intensity[x], green_house_emmissions[x], building_square_footage[x]] for x in range(len(intensity))]
sorted_intensity = sorted(intensity_list, key=lambda x: x[1])
sorted_intensity.reverse()
print(sorted_intensity)

top_intensity = [sorted_intensity[x][0] for x in range(3)]
print(top_intensity)





'''
sort_intensity = [x for x in intensity]
sort_intensity.sort()
sort_intensity.reverse()

one_intensity = intensity.index(sort_intensity[0])
two_efficient = intensity.index(sort_intensity[1])
three_efficient = intensity.index(sort_intensity[2])

print(full_schools[one_intensity][2])
print(sort_intensity[0])
'''


plt.figure(1, figsize=(12,6))
plt.scatter(building_square_footage, green_house_emmissions, alpha=0.4, s=15)
for i in range(3):
    plt.annotate(sorted_intensity[i][0], xy=(sorted_intensity[i][3], sorted_intensity[i][2]))


plt.title("Green House Emmissions vs. Building Square Footage in Chicago K-12 Schools")
plt.xlabel("Total Green House Emmissions (Metric Tons CO2e)")
plt.ylabel("Building Square Footage")

plt.show()

