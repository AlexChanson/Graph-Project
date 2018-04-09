from random import randint, sample
from math import floor
from pprint import pprint

def rd_flots():
    return randint(0, 5), randint(5, 10), randint(0, 7)

def random_level(nb_levels=5, nodes_per=(2, 10), connectivity=0.5, f=rd_flots):
    levels = []
    graph = {}
    for i in range(nb_levels):
        levels.append([])
        for j in range(randint(nodes_per[0], nodes_per[1])):
            levels[i].append(str(i) + "_" + str(j))
    for i in range(nb_levels - 1):
        level = levels[i]
        q_nb = max(1, floor(floor(connectivity * (len(level) * len(levels[i + 1]))) / len(level)))
        for node in level:
            availaible = set(levels[i + 1])
            for j in range(q_nb):
                choosen = sample(availaible, 1)[0]
                if node in graph.keys():
                    graph[node].append((choosen, f()))
                else:
                    graph[node] = [(choosen, f())]

    graph["E"] = []
    for node in levels[0]:
        graph["E"].append((node, f()))
    for node in levels[-1]:
        graph[node] = [("S", f())]

    return graph



def random(self, n, q, f=lambda x: randint(1, 10)):
    for i in range(n):
        self.graph[i] = []
    genenerated = 0

    def lam(x):
        return x[0]
    q = min(2*n*n, q)
    all_nodes = list(self.graph.keys())
    while genenerated < q:
        origin = choice(all_nodes)
        destination = origin
        while origin == destination:
            destination = choice(all_nodes)
        if destination not in map(lam, self.graph[origin]):
            genenerated += 1
            self.graph[origin].append((destination, f))
