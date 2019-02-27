import random
import math

'''
This is a simulation for a statistics class, which posed the following question.

The Penguins take a total of 20 shots, each with a 5.5% chance of scoring.
The Flyers score exactly 1 goal per game. 
Which team would you rather be?
'''

shot_odds = 0.055
simulations = 99999
pen_goals = 0
pen_wins = 0
pen_ties = 0
pen_losses = 0
prob = 0
pen_total = 0

for sims in range(simulations):
    pen_goals = 0
    for shots in range(20):
        prob = random.random()
        if prob < shot_odds:
            pen_goals += 1
            pen_total += 1
    if pen_goals > 1:
        pen_wins += 1
    elif pen_goals == 1:
        pen_ties += 1
    else:
        pen_losses += 1

pen_percentage = (pen_wins/simulations) * 100
fly_percentage = (pen_losses/simulations) * 100
tie_percentage = (pen_ties/simulations) * 100
better_team = ""

print("\n\nAfter simulating", simulations, "games...")
print("The Penguins won", pen_wins, "games with a win percentage of", round(pen_percentage, 2), "%")
print("The Flyers won", pen_losses, "games with a win percentage of", round(fly_percentage, 2), "%")
print("The two teams tied", pen_ties, "games with a tie percentage of", round(tie_percentage, 2), "%")
print("")

if pen_wins > pen_losses:
    print("In this simulation, the Penguins came out on top.")
elif pen_wins < pen_losses:
    print("In this simulation, the Flyers came out on top.")
else:
    if pen_total > simulations:
        print("In this simulation, the teams had the same number of wins. That said, the Penguins edged out the Flyers"
              ", scoring", pen_total, "goals where the Flyers scored just", simulations, ".")
    elif pen_total < simulations:
        print("In this simulation, the teams had the same number of wins. That said, the Flyers edged out the Penguins,"
              "scoring", simulations, "goals where the Penguins scored just", pen_total, ".")
    else:
        print("AND THEY SCORED THE SAME NUMBER OF GOALS,", simulations, "! WILD!")


