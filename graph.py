import pprint
import numpy
from random import randint, choice


class Graph:
    def __init__(self, dic={}):
        if dic is not None:
            self.graph = {}
            for pn, l in dic.items():
                self.graph[pn] = l
                for (node, v) in l:
                    self.graph.setdefault(node, [])
        else:
            self.graph = {}

    def empty(self):
        return Graph({})

    def addNode(self, node):
        return self.graph.setdefault(node, [])

    def getNodes(self):
        return list(set(map(lambda x: x, self.graph.keys())))

    def removeEdge(self, nodeFrom, nodeTo):
        self.graph[nodeFrom] = list(filter(lambda x: x[0] != nodeTo, self.graph.setdefault(nodeFrom, [])))

    def display(self):
        pprint.pprint(self.graph)

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
        res = list(filter(lambda x: x[0] == nodeTo, children) )
        if res:
            return res[0][1]
        else:
            return defaultValue

    def getAllEdges(self):
        return sum(list(map(lambda x: [(x[0], y[0], y[1] ) for y in x[1]] , self.graph.items())),[])

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
        if not self.nodeExists(nodeTo):
            self.addNode(nodeTo)
        return self

    def nodeNumber(self):
        return len(self.graph)

    def edgeNumber(self):
        return sum(len(x) for x in self.graph.itervalues())

    def fmap(self, f):
        returnedGraph = {}

        for (node, children) in self.graph.items():
            returnedGraph[node] = list(map(lambda x: (x[0], f(x[1])), children))
        return Graph(returnedGraph)

    def __repr__(self):
        return "Graph"





class MatrixGraph(Graph):
    def __init__(self, dic={}):
        self.nodes = set()
        self.matrix = {}
        if dic is not None:
            for pn, l in dic.items():
                self.nodes.add(pn)
                for (node, v) in l:
                    self.nodes.add(node)
                    self.matrix[(pn, node)] = v

    def empty(self):
        return MatrixGraph({})

    def addNode(self, node):
        self.nodes.add(node)

    def getNodes(self):
        return list(self.nodes)

    def removeEdge(self, nodeFrom, nodeTo):
        return self.matrix.pop((nodeFrom, nodeTo), None)

    def display(self):
        pprint.pprint(self.matrix)

    def getEdgesFrom(self, node):
        return list(map(lambda x: (x[0][1], x[1]), filter(lambda y: y[0][0] == node, self.matrix)))

    def getEdgesTo(self, node):
        return list(map(lambda x: (x[0][1], x[1]), filter(lambda y: y[0][1] == node, self.matrix)))

    def getEdgeValue(self, nodeFrom, nodeTo, defaultValue=None):
        return self.matrix.get((nodeFrom, nodeTo), defaultValue)

    def getAllEdges(self):
        return list(map(lambda x: (x[0][0], x[0][1], x[1]), self.matrix.items()))

    def nodeExists(self, node):
        return node in self.nodes

    def setEdgeValue(self, nodeFrom, nodeTo, value):
        self.addNode(nodeFrom)
        self.addNode(nodeTo)
        self.matrix[(nodeFrom, nodeTo)] = value

    def nodeNumber(self):
        return len(self.nodes)

    def edgeNumber(self):
        return len(self.matrix)

    def fmap(self, f):
        newGraph = MatrixGraph()
        newGraph.matrix = {k: f(v) for k, v in self.matrix.items()}
        return newGraph

    def __repr__(self):
        return "Matrix Graph"
