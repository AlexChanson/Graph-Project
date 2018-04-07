from pprint import pprint
from floyd import floyd2
from graph import Graph

# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    return graph.fmap(lambda x: (x[0], x[1], x[2], 0) )

def pathReconstruction(p, u, v):
    if u == v or p[(u,v)] == v:
        return []
    path = [u]
    while u != v:
        u = p[(u,v)]
        path.append(u)
    return path

def ecartGraph(graph):
    newGraph = graph.fmap(id)

    for (nodeFrom, nodeTo, v) in graph.getAllEdges():
        potential = v[1]-v[3]
        if v[3] > 0:
            newGraph.setEdgeValue(nodeTo, nodeFrom, (v[0], v[1], -v[2], v[3]))
        if potential > 0:
            newGraph.setEdgeValue(nodeFrom, nodeTo, (v[0], v[1], v[2], potential))
        else:
            newGraph.removeEdge(nodeFrom, nodeTo)
    return newGraph

def busacker_gowen(graph, entre, sortie):
    graph = getFlotNul(graph)
    V = 0
    C = 0
    found = True
    while found:
        graphEcartCalculated = ecartGraph(graph)
        #graphEcartCalculated.display()

        p, d = floyd2(graphEcartCalculated.fmap(lambda x: x[2]))

        chain = pathReconstruction(p, entre, sortie)

        deltas = list()
        for i in range(len(chain) - 1):
            suivant = graph.getEdgeValue(chain[i], chain[i+1])

            deltas.append(suivant[1] - suivant[3])
        #print("Deltas", deltas)
        delta = min(deltas, default=0)
        #print("d", delta)
        if delta <= 0:
            found = False
        else:
            for i in range(len(chain) - 1):
                suivant = graph.getEdgeValue(chain[i], chain[i+1])
                new = (suivant[0], suivant[1], suivant[2], suivant[3] + delta)
                #print("Suivant", suivant, "New", new)
                graph.setEdgeValue(chain[i], chain[i+1], new)
            #pprint(graph)

            #print(d[(entre, sortie)])
            #print(delta)
            V += delta
            C += delta * d[(entre, sortie)]
    return graph, V, C

