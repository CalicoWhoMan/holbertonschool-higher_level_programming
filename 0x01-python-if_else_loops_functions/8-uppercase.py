#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) in range (96, 123):
            x = chr(ord(x)- 32)
        print("{}".format(x), end="")
    print()
