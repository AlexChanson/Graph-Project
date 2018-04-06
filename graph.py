import pprint
from random import randint, choice


class Graph:
    def __init__(self, dic={}):
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

    def getEdgesFrom(self, node, defaultValue=[]):
        return self.graph.get(node, defaultValue)

    def getEdgesTo(self, node):
        edges = []
        for (key, children) in self.graph.items():
            for (childNode, edgeValue) in children:
                if (childNode == node):
                    edges.append((key, edgeValue))
        return edges

    def getEdgeValue(self, nodeFrom, nodeTo, defaultValue=None):
        children = self.getEdgesFrom(nodeFrom)
        res = list( filter(lambda x: x[0] == nodeTo, children) )
        if res:
            return res[0][1]
        else:
            return defaultValue

    def nodeExists(self, node):
        if self.getEdgesFrom(node, None):
            return True
        for (nodeFrom, children) in self.graph.items():
            for (nodeTo,value) in children:
                if nodeTo == node:
                    return True
        return False

    def setEdgeValue(self, nodeFrom, nodeTo, value):
        children = self.getEdgesFrom(nodeFrom, None)
        if children:
            found = False
            for i, edge in enumerate(children):
                if edge[0] == nodeTo:
                    found = True
                    children[i] = (nodeTo, value)
                    break
            if not found:
                children.append((nodeTo, value))
        else:
            self.graph[nodeFrom] = [(nodeTo, value)]
        return self

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




class MatrixGraph(Graph):
    def __init__(self, dic={}):
        if dic is not None:
            self.matrix = {}
        else:
            self.matrix = {}

    def addNode(self, label):
        pass

    def getNodes(self):
        pass

    def addEdge(self, label1, label2):
        pass

    def display(self):
        pprint.pprint(self.matrix)

    def children(self, label):
        pass

    def importCSV(self, path):
        pass

    def random(self, n, q):
        pass