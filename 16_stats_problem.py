import math
a1 = 10577235235234234294
a2 = 23397123123234234345
a3 = 343092323423423234445
a4 = 499923523235342333995

b1 = 0
b2 = 0
b3 = 0
b4 = 0



iterations = 100

for i in range(iterations):
    d1 = abs(a1 - a2)
    d2 = abs(a2 - a3)
    d3 = abs(a3 - a4)
    d4 = abs(a4 - a1)

    a1 = d1
    a2 = d2
    a3 = d3
    a4 = d4
    print(str(a1) + str(a2) + str(a3) + str(a4))
    print("")



