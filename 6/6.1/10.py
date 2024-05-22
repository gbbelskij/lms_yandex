import numpy as np


def stairs(vec):
    table = np.zeros((len(vec), len(vec)), dtype=int)
    table[0] = vec
    for i in range(1, len(vec)):
        table[i] = np.roll(table[i - 1], 1)
    return table


print(stairs(np.arange(3)))
