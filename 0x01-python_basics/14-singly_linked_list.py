#!/usr/bin/python3
"""
Node and SinglyLinkedList class definitions
"""


class Node:
    """
    class deinfition for sll node
    """
    def __init__(self, data, next_node=None):
        """
        initialization of Node class
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        data getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data setter
        """
        if value.__class__ is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node setter
        """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SinglyLinkeList class definition for a singly linked list
    """

    def __init__(self):
        """
        SinglyLinkedList class initialization
        """
        self.__head = None

    def __repr__(self):
        """
        ___repr___ for SinglyLinkedList class
        """
        retval = []
        walk = self.__head
        while walk:
            retval.append(str(walk.data))
            walk = walk.next_node
        return "\n".join(retval)

    def sorted_insert(self, value):
        """
        inserts a node into a sorted sll
        value 'data' value of node being inserted
        """
        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, next_node=self.__head)
        else:
            walk = self.__head
            while walk.next_node and walk.next_node.data < value:
                walk = walk.next_node
            new_node = Node(value, next_node=walk.next_node)
            walk.next_node = new_node
