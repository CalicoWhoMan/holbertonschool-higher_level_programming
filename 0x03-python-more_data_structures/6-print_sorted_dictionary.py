#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order_keys = sorted(a_dictionary.keys())
    for x in order_keys:
        print("{}: {}".format(x, a_dictionary[x]))
