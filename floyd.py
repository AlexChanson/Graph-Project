import numpy as np


def floyd(adj_matrix, f=lambda x:x):
    n = adj_matrix.shape[0]
    p = np.zeros(shape=(n, n))
    d = np.empty(shape=(n, n))
    d[:] = np.inf

    for i in range(n):
        for j in range(n):
            d[i, j] = f(adj_matrix(i, j))
            p[i, j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
                    p[i, j] = k

    return p, d
