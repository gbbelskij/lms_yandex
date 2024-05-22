import numpy as np


def snake(m, n, direction='H'):
    table = np.zeros((n, m), dtype=np.int16)
    count = 1
    match direction:
        case 'H':
            for i in range(n):
                if i % 2 == 0:
                    table[i] = np.arange(count, count + m)
                else:
                    table[i] = np.arange(count + m - 1, count - 1, -1)
                count += m
        case 'V':
            for j in range(m):
                if j % 2 == 0:
                    table[:, j] = np.arange(count, count + n)
                else:
                    table[:, j] = np.arange(count + n - 1, count - 1, -1)
                count += n
    return table


print(snake(5, 3))
