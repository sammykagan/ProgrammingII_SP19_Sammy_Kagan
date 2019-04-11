# Consider a row of 100 closed lockers numbered 1-100 and a line of people numbered 1-100
# Person 1 walks down the hall and opens every locker
# Person 2 then walks down the hall and closes every other locker, starting with #2
# Person 3 then walks down the hall and changes the state of every third locker, starting with #3
# (That is, they open it if it's closed and close it if it's open)
# Person 4 does the same with every fourth locker, starting with #4

# 1 = open
# 0 = closed

locker_list = [0 for x in range(100)]

person_num = 100

for i in range(1):

    person_num -= 1

    if locker_list[i] == 1:
        locker_list[i] = 0

    else:
        locker_list[i] = 1

    print(locker_list)

print(locker_list)
