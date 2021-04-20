class Tetramino:

    def __init__(self, initial_node):
        self.__actual_node = initial_node

    def rotate(self):
        self.__actual_node = self.__actual_node.next_node

    def matrix_representation(self):
        return self.__actual_node.representation
