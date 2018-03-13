import pprint

class Graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, label):
        if not self.graph.keys().__contains__(label):
            self.graph[label] = set()

    def addEdge(self, label1, label2):
        if label1 in self.graph.keys() and label2 in self.graph.keys():
            self.graph[label1].add(label2)

    def display(self):
        pprint.pprint(self.graph)

    def children(self, label):
        if label in self.graph.keys():
            return self.graph[label]
        return set()

    def depthFirst(self, start):
        visited, stack = list(), [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.graph[node] - set(visited))
        return visited

    def depthFirstIter(self):
        pass

    def breadthFirst(self, label):
        nout = []
        nmarked = set()

        def explore(node):
            children = self.children(node)
            m = list()
            #print("node=", node, "children=", children, "visited=", nmarked)
            for child in children:
                if child not in nmarked:
                    nmarked.add(child)
                    nout.append(child)
                    m.append(child)
            for child in m:
                explore(child)

        nmarked.add(label)
        nout.append(label)
        explore(label)
        return nout


    def breadthFirstIter(self):
        pass

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
