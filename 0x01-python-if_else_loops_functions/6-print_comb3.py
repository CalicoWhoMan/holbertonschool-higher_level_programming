#!/usr/bin/python3
for x in range(10):
    for a in range(10):
        if a > x:
            print("{}{}".format(x, a), end="\n" if x == 8 and a == 9 else ", ")
