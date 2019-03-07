import random
import math
simulations = 100
total_tanks = 0
append = 0
tank_ans_list = []
upper_limit = 1000
str_one = 0 #min + max
str_two = 0 # (min + max)/n
str_three = 0 # 2 * mean
str_four = 0 # 2 * median
str_five = 0
tanks_given = 7
even_tanks = False
str_one_er = 0
str_two_er = 0
str_three_er = 0
str_four_er = 0
str_five_er = 0
str_one_er_list = []
str_two_er_list = []
str_three_er_list = []
str_four_er_list = []
str_five_er_list = []
avg_er_1 = 0
avg_er_2 = 0
avg_er_3 = 0
avg_er_4 = 0
avg_er_5 = 0

for i in range(simulations):
    tank_ans_list = []
    total_tanks = random.randrange(1, upper_limit + 1)
    for j in range(tanks_given):
        add = random.randrange(1, total_tanks)
        tank_ans_list.append(add)
    tank_ans_list.sort()
    str_one = tank_ans_list[0] + tank_ans_list[tanks_given - 1]
    str_two = str_one / tanks_given
    print(str_two)
    str_three = (sum(tank_ans_list)/tanks_given) * 2
    if tanks_given % 2 == 0:
        even_tanks = True
    else:
        even_tanks = False
    if even_tanks is True:
        str_four = (tank_ans_list[tanks_given//2] + tank_ans_list[(tanks_given//2) + 1])
    else:
        str_four = tank_ans_list[tanks_given//2]
    str_five = tank_ans_list[tanks_given-1] + ((tank_ans_list[tanks_given-1] ** (3/2))/2)

    str_one_er = abs(str_one - total_tanks)
    str_one_er_list.append(str_one_er)

    str_two_er = abs(str_two - total_tanks)
    str_two_er_list.append(str_two_er)

    str_three_er = abs(str_three - total_tanks)
    str_three_er_list.append(str_three_er)

    str_four_er = abs(str_four - total_tanks)
    str_four_er_list.append(str_four_er)

    str_five_er = abs(str_five - total_tanks)
    str_five_er_list.append(str_five_er)

avg_er_1 = (sum(str_one_er_list))/simulations
avg_er_2 = (sum(str_two_er_list))/simulations
avg_er_3 = (sum(str_three_er_list))/simulations
avg_er_4 = (sum(str_four_er_list))/simulations
avg_er_5 = (sum(str_five_er_list))/simulations

print("Average 1 Error:", avg_er_1)
print("Average 2 Error:", avg_er_2)
print("Average 3 Error:", avg_er_3)
print("Average 4 Error:", avg_er_4)
print("Average 5 Error:", avg_er_5)



