# the three dimensional list below contains a secret message.
# The secret message is made up of #'s and spaces
# Decode and print the message.  You will know when you got it right.
# Good luck!

decode_me = [[[' ', 1], ['#', 8], [' ', 1], ['#', 8], [' ', 5], ['#', 3], [' ', 4], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 6], [' ', 2], ['#', 4], [' ', 2], ['#', 6]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 3], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 2], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 4], [' ', 2], ['#', 2], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 2], ['#', 2]], [[' ', 1], ['#', 6], [' ', 3], ['#', 8], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 3], ['#', 6]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 3], ['#', 2], [' ', 3], ['#', 9], [' ', 1], ['#', 2], [' ', 2], ['#', 4], [' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 8], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 3], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 2], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 6], [' ', 2], ['#', 4], [' ', 2], ['#', 6]], [[' ', 1], ['#', 8], [' ', 5], ['#', 3], [' ', 4], ['#', 8], [' ', 2], ['#', 2], [' ', 4], ['#', 2], [' ', 1], ['#', 8], [' ', 1], ['#', 8]], [[' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 3], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2]], [[' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 7], ['#', 2], [' ', 5], ['#', 2]], [[' ', 1], ['#', 8], [' ', 2], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 8], [' ', 2], ['#', 5], [' ', 4], ['#', 6], [' ', 3], ['#', 8]], [[' ', 1], ['#', 2], [' ', 8], ['#', 9], [' ', 1], ['#', 2], [' ', 3], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 7], ['#', 2], [' ', 3], ['#', 2]], [[' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 2], ['#', 2], [' ', 3], ['#', 2], [' ', 2], ['#', 2], [' ', 7], ['#', 2], [' ', 4], ['#', 2]], [[' ', 1], ['#', 2], [' ', 8], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 5], ['#', 2], [' ', 1], ['#', 2], [' ', 4], ['#', 2], [' ', 1], ['#', 8], [' ', 1], ['#', 2], [' ', 5], ['#', 2]]]



for j in range(len(decode_me)):
    for i in range(len(decode_me)):
        for k in range(decode_me[j][i][1]):
            print(decode_me[j][i][0], end = "")
    print("")
