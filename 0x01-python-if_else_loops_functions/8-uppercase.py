#/usr/bin/python3
def uppercase(str):
    for x in str:
        if 97 <= ord(char) <= 122:
            a = chr(ord(x) -32)
        else:
            a = x
        print("{}".format(a), end="")
    print("")
