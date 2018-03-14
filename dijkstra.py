from graph import Graph


demo = {1:[(2, 10), (3,3), (5,6)],
        2:[(1,0)],
        3:[(2,4), (5,2)],
        4:[(3,4), (5,3)],
        5:[(2,0), (6,1)],
        6:[(1,2), (2,1)]}


def minimum(M, d):
    chosen, minimum = None, None
    for key, value in d.items():
        if key in M:
            if minimum is None:
                chosen, minimum = key, value
            elif value < minimum:
                chosen, minimum = key, value
    return chosen, minimum


def dijkstra(graph, source):
    F = {source}
    S = graph.getNodes()
    M = S - F

    d = {}

    d[source] = 0
    for child, weight in graph.children(source):
        d[child] = weight

    p = {}
    for item in S:
        p[item] = 1

    while len(M) > 0:
        m, dm = minimum(M, d)
        if m is None:
            break
        else:
            M.remove(m)
            for child, value in graph.children(m):
                if child in M:
                    cout = dm + value
                    if cout < d.get(child, cout + 1):
                        d[child] = cout
                        p[child] = m
    return p, d


G = Graph()
G.random(10000, 500000)

dijkstra(G, 1)

