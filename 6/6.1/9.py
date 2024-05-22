import numpy as np


def rotate(matrix, angle):
    turns = angle // 90
    return np.rot90(matrix, 4 - turns)

print(rotate(np.arange(12).reshape(3, 4), 270))
