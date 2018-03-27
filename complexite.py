from graph import Graph
import testData
import dijkstra
import flots
from pprint import pprint


# Demo code goes here
def identity(x):
    return x

# Dijkstra
pprint(dijkstra.dijkstra(Graph(testData.demo), 1, identity))

#Flots
soluce = flots.busacker_gowen(testData.flots, "E", "R")
pprint(soluce)