#!/usr/bin/python3
"""
module containing Node and SinglyLinkdeList classes
"""


class Node:
    """
    defines a node in a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        node initialization
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter for node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        setter for data attribute
        @value: integer
        """
        if value.__class__ is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        getter for node node_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        setter for next_node attribute
        @next_node: Node object or None
        """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """
    defines a singly linked list
    """
    def __init__(self):
        """
        linked list initialization
        """
        self.__head = None

    def __repr__(self):
        """
        returns the node data in the singly linked list
        """
        node_list = []
        i = self.__head
        while i is not None:
            node_list.append(str(i.data))
            i = i.next_node
        return '\n'.join(node_list)

    def sorted_insert(self, value):
        """
        inserts a node into the list in increasing order
        """
        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, next_node=self.__head)
        else:
            walk = self.__head
            while walk.next_node and walk.next_node.data < value:
                walk = walk.next_node
            new_node = Node(value, next_node=walk.next_node)
            walk.next_node = new_node
