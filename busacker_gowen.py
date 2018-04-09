from pprint import pprint
from floyd import floyd2
from graph import Graph

# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    return graph.fmap(lambda x: (x[0], x[1], x[2], 0) )

def pathReconstruction(p, u, v):
    if p.get((u,v), None) is None:
        return []
    path = [u]
    while u != v:
        u = p[(u,v)]
        print(u)
        path.append(u)
    return path

def ecartGraph(graph):
    newGraph = Graph()
    for node in graph.getNodes():
        newGraph.addNode(node)
    for (x, y, v) in graph.getAllEdges():
        _min, _max, cout, current = v
        if _max - current > 0:
            val = cout * (_max - current)
            newGraph.setEdgeValue(x, y, val)
        if current > 0:
            val = cout * (current - _min)
            newGraph.setEdgeValue(y, x, -val)

    return newGraph

import math

nit = 0

def busacker_gowen(graph, entre, sortie):
    graph = getFlotNul(graph)
    flux = 0
    cout = 0
    while True:
        print("graphe ecart")
        graphEcartCalculated = ecartGraph(graph)

        print("floyd")
        p, d = floyd2(graphEcartCalculated.fmap(float))

        print("path")
        chain = pathReconstruction(p, entre, sortie)
        print(chain)
        deltas = list()
        for i in range(len(chain) - 1):
            suivant = graph.getEdgeValue(chain[i], chain[i+1])
            value = suivant[3]
            deltas.append(suivant[1] - suivant[3])
        delta = min(deltas, default=0)
        if delta <= 0:
            break

        print("for 2")
        for i in range(len(chain) - 1):
            _min, _max, _unit_cost, _current = graph.getEdgeValue(chain[i], chain[i+1])
            new = (_min, _max, _unit_cost, _current + delta)
            graph.setEdgeValue(chain[i], chain[i+1], new)
        print("fin for 2")
        flux += delta
        cout += delta * d[(entre, sortie)]
    global nit
    nit += 1
    print(nit)
    return graph, flux, cout

