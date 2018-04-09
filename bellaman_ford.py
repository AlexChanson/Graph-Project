from graph import Graph


def bellmanFord(graph: Graph, source):
    inf = float('inf')
    d = {}
    p = {}

    for vertex in graph.graph.keys():
        d[vertex] = inf
        p[vertex] = None

    d[source] = 0

    for i in range(graph.nodeNumber() - 1):
        for u, v, tag in graph.getAllEdges():
            if d[u] + tag < d[v]:
                d[v] = d[u] + tag
                p[v] = u

    for u, v, w in graph.getAllEdges():
        if d[u] + w < d[v]:
            raise Exception("Cycle absorbant !")

    return p, d
