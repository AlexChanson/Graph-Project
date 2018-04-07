import numpy as np
from graph import *


def cout(graph, i, j):
    pass


def floyd(graph):
    n = graph.countNodes()
    p = np.zeros(shape=(n, n))
    d = np.empty(shape=(n, n))
    d[:] = np.inf

    for i in range(n):
        for j in range(n):
            d[i, j] = cout(graph, i, j)
            p[i, j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
                    p[i, j] = k


def floyd2(graph):
    allnodes = graph.getNodes()
    n = len(allnodes)
    p = np.zeros(shape=(n, n))
    d = np.empty(shape=(n, n))

    for i in range(n):
        for j in range(n):
            edgeVal = graph.getEdgeValue()
            d[i, j] = edgeVal
            p[i, j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i, k] + d[k, j] < d[i, j]:
                    d[i, j] = d[i, k] + d[k, j]
                    p[i, j] = k