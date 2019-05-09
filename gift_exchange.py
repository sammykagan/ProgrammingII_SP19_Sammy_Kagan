import random
import math
sims = 10000000
own_name_total = 0
people = 18
unique_draw = 0

for i in range(sims):
    if i % 10000 == 0:
        print(str(i) + " simulations complete.")
        print(str((i/sims)*100) + "% done.")

    gift_list = []
    gift_list_2 = []
    for i in range(1,people+1):
        gift_list.append(i)
    random.shuffle(gift_list)

    for i in range(1,people+1):
        gift_list_2.append(i)
    random.shuffle(gift_list_2)
    own_name = 0

    for i in range(len(gift_list)):
        if gift_list[i] == gift_list_2[i]:
            own_name += 1

    own_name_total += own_name

    if own_name == 0:
        unique_draw += 1

odds = own_name_total/sims


print("After " + str(sims) + " simulations, in a group of " + str(people)+ " on average, " + str(odds) +
      " people will draw their own name.")

odds_unique = unique_draw/sims

recip = 1/odds_unique
e_margin = recip/math.e


print("The odds nobody will draw their own name is " + str(odds_unique))
print("The reciprocal of the odds is " + str(recip))
print("The reciprocal is " + str(e_margin) + "% of e.")



