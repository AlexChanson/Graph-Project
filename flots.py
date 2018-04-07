from pprint import pprint
from floyd import floyd2
from graph import Graph

# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    flot = dict()
    for key in graph.keys():
        l = []
        # pprint(graph[key])
        for e in graph[key]:
            l.append((e[0], (e[1][0], e[1][1], e[1][2], 0)))
        flot[key] = l

    return flot



    print(r)

def pathReconstruction(p, u, v):
    if u is v:
        return []
    path = [u]
    while u is not v:
        u = p[(u,v)]
        path.append(u)
    return path

def busacker_gowen(graph, entre, sortie):
    graph = getFlotNul(graph)
    V = 0
    C = 0
    found = True
    while found:
        p, d = floyd2(Graph(graph).fmap(lambda x: x[2]*x[3]))

        chain = pathReconstruction(p, entre, sortie)

        deltas = list()
        for i in range(len(chain) - 1):
            suivant = list(filter(lambda x: x[0] == chain[i + 1], graph[chain[i]]))[0]
            # print(suivant)
            deltas.append(suivant[1][1] - suivant[1][3])
        print(chain)
        print("Deltas", deltas)
        delta = min(deltas)
        #print("d", delta)
        if delta <= 0:
            found = False
        else:
            for i in range(len(chain) - 1):
                suivant = list(filter(lambda x: x[0] == chain[i + 1], graph[chain[i]]))[0]
                new = (suivant[0], (suivant[1][0], suivant[1][1], suivant[1][2], suivant[1][3] + delta))
                #print("Suivant", suivant, "New", new)
                graph[chain[i]].remove(suivant)
                graph[chain[i]].append(new)
            #pprint(graph)

            print(d[(entre, sortie)])
            print(delta)
            V += delta
            C += delta * d[(entre, sortie)]
    return graph, V, C

