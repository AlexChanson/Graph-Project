import pprint
import random as rd


class Graph:
    def __init__(self, dic=None):
        if dic is not None:
            self.graph = dic
        else:
            self.graph = {}

    def addNode(self, label):
        if not self.graph.keys().__contains__(label):
            self.graph[label] = set()

    def getNodes(self):
        return self.graph.keys()

    def addEdge(self, label1, label2):
        if label1 in self.graph.keys() and label2 in self.graph.keys():
            self.graph[label1].add(label2)

    def display(self):
        pprint.pprint(self.graph)

    def children(self, label):
        if label in self.graph.keys():
            return self.graph[label]
        return set()

    def importCSV(self, path):
        with open(path, mode="r") as file:
            lines = file.readlines()

        for line in lines:
            left, right = line.split(",")
            left = left.strip("\n")
            right = right.strip("\n")
            if left not in self.graph.keys():
                self.graph[left] = set()
            if right not in self.graph.keys():
                self.graph[right] = set()
            self.graph[left].add(right)

    def random(self, n, q, f=lambda x: rd.randint(1, 10)):
        for i in range(n):
            self.graph[i] = []
        genenerated = 0

        def lam(x):
            return x[0]
        q = min(2*n*n, q)
        all_nodes = list(self.graph.keys())
        while genenerated < q:
            origin = rd.choice(all_nodes)
            destination = origin
            while origin == destination:
                destination = rd.choice(all_nodes)
            if destination not in map(lam, self.graph[origin]):
                genenerated += 1
                self.graph[origin].append((destination, f))


