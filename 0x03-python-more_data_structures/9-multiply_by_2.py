#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_language = a_dictionary.copy()
    for x in new_language:
        new_language[x] *= 2
    return new_language    
