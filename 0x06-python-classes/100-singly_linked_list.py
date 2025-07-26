#!/usr/bin/python3
"""The Path to python3"""


class Node:
    """The Node class"""
    def __init__(self, data, next_node=None):
        """Instatiating the date and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method that retrieve data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value to data after validating it"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setters"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Linked list class"""
        self.__head = None

    def sorted_insert(self, value):
        """Sort the node in ascending order"""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while ((current.next_node is not None) and
                   (current.next_node.data < value)):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """print the nodes"""
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
