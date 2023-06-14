#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''function that prints a dictionary by ordered keys.

    Args:
        a_dictionary: data structure being considered

    Return:
        one on a line sorted keys with their values
    '''

    for i, j in sorted(a_dictionary.items()):
        print("{:s}: {}".format(i, j))
