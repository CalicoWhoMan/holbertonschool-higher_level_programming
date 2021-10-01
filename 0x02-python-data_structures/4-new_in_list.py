#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    next_list = my_list.copy()
    if idx < 0:
        return next_list
    elif idx >= len(my_list):
        return next_list
    else:
        next_list[idx] = element
        return next_list
