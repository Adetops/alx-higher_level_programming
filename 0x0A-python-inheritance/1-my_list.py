#!/usr/bin/python3
''' Module that defines the inheriting class MyList'''


class MyList(list):
    ''' This is a class defined as a subclass.

    Method:
        print_sorted(self): This method prints the list in sorted order.

    Example:
        my_list = MyList()
    '''

    def print_sorted(self):
        '''
        prints a specified list in sorted order.
        '''

        print(sorted(self))
