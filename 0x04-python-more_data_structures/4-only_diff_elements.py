#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''returns a set of all elements present in only one set.

    Args:
        set_1: first set
        set_2: second set

    Return:
        The set of all elements not common to both set_1 and set_2
    '''

    return (set_1 ^ set_2)
