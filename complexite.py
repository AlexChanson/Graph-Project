from Graph import Graph

g = Graph()
g.importCSV("test.csv")

g.display()
print(g.depthFirst('1'))
print(g.breadthFirst('1'))
