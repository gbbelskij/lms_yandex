import numpy as np

def multiplication_matrix(n):
    multi = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            multi[i, j] = (i + 1) * (j + 1)
    return multi

n = int(input())
print(multiplication_matrix(n))
