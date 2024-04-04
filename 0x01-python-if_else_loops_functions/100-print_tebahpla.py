#!/usr/bin/python3
for Alpha in range(ord('z'), ord('a')-1, -1):
    if Alpha % 2 == 0:
        asci = 0
    else:
        asci = 32
    print('{}'.format(chr(Alpha - asci)), end="")
