#!/usr/bin/python3
def number_keys(a_dictionary):
    '''returns the number of keys in a dictionary.

    Args:
        a_dictionary: dictionary to count from

    Return:
        The total number of keys in the dict
    '''

    return (len(set(a_dictionary)))
