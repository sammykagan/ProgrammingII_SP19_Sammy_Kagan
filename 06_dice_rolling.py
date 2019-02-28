import math
import random

simulations = 1000
die = 0
die_list = []
sims = 0
sim_total = 0
average_sims = 0

for i in range(simulations):
    while len(die_list) < 6:
        die = random.randrange(1, 7)
        if die not in die_list:
            die_list.append(die)
        sims += 1
    sim_total += sims
    sims = 0
    die_list = []
average_sims = sim_total/simulations

print("\n\nAfter", simulations, "simulations, he average number of rolls necessary was", average_sims)


columns = 10000
outcome = 0
sim = -1
ev = 0

for i in range(columns):
    sim += 1
    outcome = (1/6)*((5/6) ** sim) * (sim + 1)
    ev += outcome
print("\nThe expected value of finding the 6th distinct result after", columns, "columns is", round(ev,2))

columns_1 = 10000
outcome_1 = 0
sim_1 = -1
ev_1 = 0

for i in range(columns):
    sim_1 += 1
    outcome_1 = (1/3)*((2/3) ** sim_1) * (sim_1 + 1)
    ev_1 += outcome_1
print("\nThe expected value of finding the 5th distinct result after", columns_1, "columns is", round(ev_1,2))

columns_2 = 10000
outcome_2 = 0
sim_2 = -1
ev_2 = 0

for i in range(columns):
    sim_2 += 1
    outcome_2 = (1/2)*((1/2) ** sim_2) * (sim_2 + 1)
    ev_2 += outcome_2
print("\nThe expected value of finding the 4th distinct result after", columns_2, "columns is", round(ev_2,2))

columns_3 = 10000
outcome_3 = 0
sim_3 = -1
ev_3 = 0

for i in range(columns):
    sim_3 += 1
    outcome_3 = (2/3)*((1/3) ** sim_3) * (sim_3 + 1)
    ev_3 += outcome_3
print("\nThe expected value of finding the 3rd distinct result after", columns_3, "columns is", round(ev_3,2))

columns_4 = 10000
outcome_4 = 0
sim_4 = -1
ev_4 = 0

for i in range(columns):
    sim_4 += 1
    outcome_4 = (5/6)*((1/6) ** sim_4) * (sim_4 + 1)
    ev_4 += outcome_4
print("\nThe expected value of finding the 2nd distinct result after", columns_4, "columns is", round(ev_4,2))

columns_5 = 10000
outcome_5 = 0
sim_5 = -1
ev_5 = 0

for i in range(columns):
    sim_5 += 1
    outcome_5 = (6/6)*((0/6) ** sim_5) * (sim_5 + 1)
    ev_5 += outcome_5
print("\nThe expected value of finding the 1st distinct result after", columns_5, "columns is", round(ev_5,2))




