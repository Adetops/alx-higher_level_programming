#!/usr/bin/python3
"""Defining a singly linked list. """


class Node:
    """Setting up the node class """

    def __init__(self, data, next_node=None):
        """ Initializing the node

        Args:
            data (int): integer value
            next_node (pointer): pointer to the next node
        """

        self.data = data
        self.next_node = next_node

    @property
    """ To set and get the data value """

    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    """ To set and get the next_node pointer. """

    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and (value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defining a singly linked list that'll implement the node """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if (self.__head is None):
            new.next_node = None
            self.__head = new
        elif (self.__head.data > value):
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node != None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
