#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''adds all unique integers in a list (only once for each integer).

    Args:
        my_list: the list to consider

    Return:
        The sum of all the integers
    '''
    addition = 0
    for i in set(my_list):
        addition += i
    return (addition)
