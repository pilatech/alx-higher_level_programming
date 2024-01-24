#!/usr/bin/python3
"""Define singly linked list"""


class Node:
    """Definition of a Node for a singly linked list
    Attributes:
        __data (int): the data.
        __next_node (Node): the link to next node.
    """
    def __init__(self, data, next_node=None):
        """Initialize the size.
        Args:
            data (int): the number to store.
            next_node (node): link to the next node
        Returns: None
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data

        if (next_node is not None) and (type(next_node) is not Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node
    @property
    def data(self):
        """Get the data value
        Returns: the data value
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value
        Returns: None
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Get the not value
        Returns: the data value
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node value
        Returns: None
        """
        if (self.__next_node is not None) and (type(value) is not Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    

class SinglyLinkedList:
    """Definition of a singly linked list
    Attributes:
        __head (node): the start of the list.
    """
    def __init__(self):
        """Initialize a singly linked list
        Resturns: None
        """
        self.__head = None

    def __str__(self):
        """Print the linked list
        Returns: None
        """
        val = ""
        temp = self.__head
        while temp:
            val = val + str(temp.data)
            if temp.next_node:
                val = val + "\n"
            temp = temp.next_node
        return val
    
    def sorted_insert(self, value):
        """Insert a node into a sorted linked list
        Attributes:
            value (int): the number to insert.
        Returns: None
        """
        temp = self.__head
        new_node = Node(value)

        if temp is None:
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = temp.next_node
            self.__head = new_node

        else:
            while temp:
                if temp.next_node:
                    if temp.data <= value and temp.next_node.data > value:
                        new_node.next_node = temp.next_node
                        temp.next_node = new_node
                else:
                    temp.next_node = new_node
                    temp = temp.next_node











