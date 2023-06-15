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

    a_dictionary[key] = value
    return (a_dictionary)
