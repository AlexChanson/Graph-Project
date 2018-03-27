from pprint import pprint

# Prend un graphe et retourne le flot nul correspondant
def getFlotNul(graph):
    flot = dict()
    for key in graph.keys():
        l = []
        #pprint(graph[key])
        for e in graph[key]:
            l.append((e[0], (e[1][0], e[1][1], e[1][2], 0)))
        flot[key] = l

    return flot


def busacker_gowen(graph, entre, sortie):
    from dijkstra import dijkstra
    from graph import Graph
    graph = getFlotNul(graph)
    V = 0
    C = 0
    found = True
    while found:
        p, d = dijkstra(Graph(graph), entre, lambda x: x[3]*x[2])
        current = p[sortie]
        chain = [current, sortie]
        #print(p)
        while current is not entre:
            current = p[current]
            chain.insert(0, current)
        #print("Chain", chain)
        deltas = list()
        for i in range(len(chain) - 1):
            suivant = list(filter(lambda x : x[0] == chain[i+1], graph[chain[i]]))[0]
            #print(suivant)
            deltas.append(suivant[1][1] - suivant[1][3])
        #print("Deltas", deltas)
        delta = min(deltas)
        print("d", delta)
        if delta <= 0:
            found = False
        else:
            for i in range(len(chain) - 1):
                suivant = list(filter(lambda x: x[0] == chain[i + 1], graph[chain[i]]))[0]
                new = (suivant[0], (suivant[1][0], suivant[1][1], suivant[1][2], suivant[1][3] + delta))
                print("Suivant", suivant, "New", new)
                graph[chain[i]].remove(suivant)
                graph[chain[i]].append(new)
            pprint(graph)

            V += delta
            C += delta*len(chain)
    return graph

