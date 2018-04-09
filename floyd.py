import numpy as np
import math

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


def tryAdd(a, b):
    if math.isfinite(a) and math.isfinite(b):
        return a + b
    return math.inf

from pprint import pprint

def floyd2(graph):
    allnodes = list(graph.getNodes())
    p = {}
    d = {}

    for (i, j, v) in graph.getAllEdges():
        d[(i, j)] = v
        p[(i, j)] = j

    for k in allnodes:
        for i in allnodes:
            for j in allnodes:
                g = d.get((i, j), math.inf)
                h = tryAdd(d.get((i, k), math.inf) ,d.get((k, j), math.inf))
                if h < g:
                    d[(i, j)] = h
                    p[(i, j)] = p[(i,k)]
    return p, d