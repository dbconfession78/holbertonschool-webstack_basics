#!/usr/bin/python3
"""
Module 14-singly_linked_list
"""


class Node:
    """
    Node: class deinfition for sll node
    """
    def __init__(self, next_node=None):
        """
        initialization of Node class
        """
        self.__data = None
        self.__next_node = next_node

    @property
    def data(self):
        """
        data: getter
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data: setter
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node: getter
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        next_node: setter
        """
        if type(value) not in {Node, None}:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkeList: class definition for a singly linked list
    """
    __head = None

    def __init__(self):
        """
        SinglyLinkedList class initialization
        """
        pass
#        self.__head = None

    def __repr__(self):
        """
        ___repr___ for SinglyLinkedList class
        """
        print("there")
        return self

    def __str__(self):
        """
        ___str___ for SinglyLinkedList class
        """

        retval = ""
        walk = self.__head
        while walk:
            retval += "{}".format(str(walk.data))

            if walk.next_node is not None:
                retval += "\n"
            walk = walk.next_node
        return "{}".format(retval)

    def sorted_insert(self, value):
        """
        inserts a node into a sorted sll
        :value: 'data' value of node being inserted
        """
        new_node = Node()
        new_node.data = value
        if self.__head is None:
            self.__head = new_node
        else:
            walk = self.__head
            prev = None
            while walk:
                if walk.data >= value:
                    if prev:
                        prev.next_node = new_node
                    else:
                        self.__head = new_node
                    new_node.next_node = walk
                    break
                if prev is None and walk.data >= value:
                    self.head = new_node
                    new_node.next_node = walk
                    break
                prev = walk
                if walk.next_node:
                    if walk.next_node.data >= value:
                        new_node.next_node = walk.next_node
                        walk.next_node = new_node
                        break
                    else:
                        walk = walk.next_node
                else:
                    walk.next_node = new_node
                    break
