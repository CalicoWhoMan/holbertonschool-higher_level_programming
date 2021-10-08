#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    other_num = number % -10
else:
    other_num = number % 10
if other_num == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif other_num < 6:
    print("Last digit of {} is {}".format(number, other_num), end=" ")
    print("and is less than 6 and not 0")
else:
    print("Last digit of {} is {}".format(number, other_num), end=" ")
    print("and is greater than 5")
