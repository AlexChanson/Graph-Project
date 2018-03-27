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

