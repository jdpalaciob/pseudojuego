import numpy as np

from model.Tetramino import Tetramino
from model.Node import Node

up_node_representation = np.array(
    [
        [0, 1, 1],
        [1, 1, 0]
    ]
)

down_node_representation = np.array(
    [
        [1, 0],
        [1, 1],
        [0, 1],
    ]
)

up_node = Node(up_node_representation)
down_node = Node(down_node_representation)

up_node.next_node = down_node
down_node.next_node = up_node


class STetramino(Tetramino):

    def __init__(self):
        super().__init__(up_node)
