#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dictionary to update
        key: always a string (to add)
        value: any data type (to add)

    Return:
        The updated dictionary
    '''

    for j, l in a_dictionary.items():
        if j == key:
            l = value
        elif key not in a_dictionary:
            a_dictionary = dict(a_dictionary, key=value)
    return (a_dictionary)
