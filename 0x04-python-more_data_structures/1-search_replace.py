#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''  replaces all occurrences of an element by another in a new list

    Args:
        my_list: the initial list
        search: element to replace in the list
        replace: the new element

    Return:
        A new list with 'search' replaced
    '''
    new_list = []
    for i, j in enumerate(my_list):
        if j == search:
            j = replace
        new_list.append(j)
    return (new_list)
