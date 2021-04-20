class Node:

    def __init__(self, representation, next_node=None):
        self.representation = representation
        self.__next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node
