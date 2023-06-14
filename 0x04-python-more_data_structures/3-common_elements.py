#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''returns a set of common elements in two sets.

    Args:
        set_1: the first set
        set_2: second set

    Return:
        The set of common elements in set_1 and set_2
    '''

    return (x for x in set_1 if x in set_2)
