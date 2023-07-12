#!/usr/bin/python3
''' Module that defines the inheriting class MyList'''


class MyList(list):
    ''' This is a class defined as a subclass.

    This subclass inherits from the superclass 'list'.

    Method:
        print_sorted(self): This method prints the list in sorted order.
    
    Example:
        my_list = MyList()
    '''


    def print_sorted(self):
        ''' prints a specified list in sorted order.

        This method takes no argument
        '''

        print(sorted(self))
