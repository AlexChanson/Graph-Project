from pprint import pprint
from floyd import floyd2
from graph import Graph

# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    return graph.fmap(lambda x: (x[0], x[1], x[2], 0) )

def pathReconstruction(p, u, v):
    if u == v:
        return []
    path = [u]
    while u != v:
        u = p[(u,v)]
        path.append(u)
    return path

def ecartGraph(graph):
    pass

def busacker_gowen(graph, entre, sortie):
    graph = getFlotNul(graph)
    V = 0
    C = 0
    found = True
    while found:
        p, d = floyd2(graph.fmap(lambda x: (x[1]-x[2])*x[3]))

        chain = pathReconstruction(p, entre, sortie)

        deltas = list()
        for i in range(len(chain) - 1):
            suivant = graph.getEdgeValue(chain[i], chain[i+1])
            deltas.append(suivant[1] - suivant[3])
        print(chain)
        print("Deltas", deltas)
        delta = min(deltas)
        print("d", delta)
        if delta <= 0:
            found = False
        else:
            for i in range(len(chain) - 1):
                suivant = graph.getEdgeValue(chain[i], chain[i+1])
                new = (suivant[0], suivant[1], suivant[2], suivant[3] + delta)
                #print("Suivant", suivant, "New", new)
                graph.setEdgeValue(chain[i], chain[i+1], new)
            #pprint(graph)

            print(d[(entre, sortie)])
            print(delta)
            V += delta
            C += delta * d[(entre, sortie)]
    return graph, V, C

