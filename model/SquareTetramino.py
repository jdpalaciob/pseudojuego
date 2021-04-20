import numpy as np

from model.Tetramino import Tetramino
from model.Node import Node

node_representation = np.array(
    [
        [1, 1],
        [1, 1]
    ]
)

initial_node = Node(node_representation)
initial_node.next_node = initial_node


class SquareTetramino(Tetramino):

    def __init__(self):
        super().__init__(initial_node)
