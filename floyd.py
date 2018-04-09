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
    if math.isfinite(float(a)) and math.isfinite(float(b)):
        return a + b
    return math.inf

def floyd2(graph):
    allnodes = graph.getNodes()
    n = len(allnodes)
    p = {}
    d = {}

    for i in allnodes:
        for j in allnodes:
            edgeVal = graph.getEdgeValue(i, j, math.inf) if i != j else 0
            d[(i, j)] = edgeVal
            p[(i, j)] = j

    for k in allnodes:
        for i in allnodes:
            for j in allnodes:
                g = d[(i, j)]
                h = tryAdd(d.get((i, k)) ,d.get((k, j)))
                if h < g:
                    d[(i, j)] = h
                    p[(i, j)] = p[(i,k)]
    return p, d