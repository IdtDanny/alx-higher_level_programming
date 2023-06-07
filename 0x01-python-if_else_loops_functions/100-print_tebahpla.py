#!/usr/bin/python3
x = 0
for alpha in range(122, 96, -1):
    print("{}".format(chr(alpha - x)), end="")
    x = 32 if x == 0 else 0
