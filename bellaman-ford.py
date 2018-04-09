from graph import Graph


def bellmanFord(graph : Graph, source, f=lambda x:x):
    inf = float('inf')
    d = {}
    p = {}

    for vertex in graph.graph.keys():
        d[vertex] = inf
        p[vertex] = None

    d[source] = 0

    for vertex in graph.graph.keys():
        for edge in graph.graph[vertex]:
            if vertex == source:
                d[edge[0]] = f(edge[1])
            elif d[vertex] != inf:
                pass
