from pprint import pprint
from floyd import floyd2
from graph import Graph
from bellaman_ford import bellmanFord


# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    return graph.fmap(lambda x: (float(x[0]), float(x[1]), float(x[2]), 0.0))


def pathReconstruction(p, u, v):
    if p.get((u,v), None) is None:
        return []
    path = [u]
    while u != v:
        u = p[(u, v)]
        path.append(u)
    return path


def ecart_graph(graph):
    new_graph = Graph()
    for node in graph.getNodes():
        new_graph.addNode(node)
    for (x, y, v) in graph.getAllEdges():
        _min, _max, cout, current = v
        if _max - current > 0:
            val = cout * (_max - current)
            new_graph.setEdgeValue(x, y, val)
        if current > 0:
            val = cout * ( current - _min )
            new_graph.setEdgeValue(y, x, val)
    return new_graph


def busacker_gowen(graph, entre, sortie):
    graph = getFlotNul(graph)
    flux = 0.0
    cout = 0.0
    while True:
        p, d = bellmanFord(ecart_graph(graph), "E")

        current = sortie
        chain = []
        while current != entre:
            chain.insert(0, current)
            current = p[current]
            if current is None:
                break

        deltas = list()
        for i in range(len(chain) - 1):
            suivant = graph.getEdgeValue(chain[i], chain[i + 1])
            if suivant is not None:
                deltas.append(suivant[1] - suivant[3])
            else:
                suivant = graph.getEdgeValue(chain[i + 1], chain[i])
                deltas.append(suivant[1] - suivant[3])
        delta = min(deltas, default=0)
        if delta <= 0:
            break

        for i in range(len(chain) - 1):
            edge = graph.getEdgeValue(chain[i], chain[i + 1])
            if edge is None:
                edge = graph.getEdgeValue(chain[i + 1], chain[i])
                _min, _max, _unit_cost, _current = edge
                new = (_min, _max, _unit_cost, _current - delta)
            else:
                _min, _max, _unit_cost, _current = edge
                new = (_min, _max, _unit_cost, _current + delta)

            graph.setEdgeValue(chain[i], chain[i + 1], new)

        flux += delta
        cout += delta * d[sortie]

    return graph, flux, cout


busacker_gowen.__setattr__("authors", ["Ben Crulis", "Alexandre Chanson"])
