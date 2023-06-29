#!/usr/bin/python3
"""Defining a singly linked list. """


class Node:
    """Setting up the node class """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node()) and (value != None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:

    def __init__(self):
        self.__head = head
        print(head)

    def sorted_insert(self, value):
        self.__value = value

        alist = []
        alist.append(self.__value)
