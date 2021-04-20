from random import choice
from model import SquareTetramino, LLeftTetramino, LineTetramino, LRightTetramino, STetramino, ZTetramino, TTetramino


def generate_tetramino():
    tetramino = choice(
        (
            SquareTetramino.SquareTetramino(),
            LLeftTetramino.LLeftTetramino(),
            LineTetramino.LineTetramino(),
            LRightTetramino.LRightTetramino(),
            STetramino.STetramino(),
            ZTetramino.ZTetramino(),
            TTetramino.TTetramino()
        )
    )
    return tetramino.matrix_representation()
