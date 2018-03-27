from graph import Graph

# paire (destination, cout)
demo = {1: [(2, 10), (3, 3), (5, 6)],
        2: [(1, 0)],
        3: [(2, 4), (5, 2)],
        4: [(3, 4), (5, 3)],
        5: [(2, 0), (6, 1)],
        6: [(1, 2), (2, 1)]}

# quadruplet (destination, min, max, cost)
flots = {
    "S1": [("S2", 0, 2, 0), ("T1", 0, 3, 0)],
    "S2": [("T1", 0, 1, 0), ("T2", 0, 1, 0), ("T3", 0, 1, 0)],
    "S3": [("S2", 0, 2, 0), ("T3", 0, 3, 0)],
    "T1": [("T2", 0, 2, 0), ("T4", 0, 7, 0)],
    "T2": [("T4", 0, 2, 0), ("T5", 0, 1.5, 0)],
    "T3": [("T2", 0, 3, 0), ("T5", 0, 1, 0)],
    "T4": [("R", 0, 8, 0)],
    "T5": [("R", 0, 5, 0)],
    "S": [("S1", 0, 5, 0), ("S2", 0, 4, 0), ("S3", 0, 3, 0)]
}


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

    d = {source: 0}

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
