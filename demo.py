import graph
import fordFulkerson as ff
import busacker_gowen as bg
import graphGen
from eval import *

def tall_networks(n):
    return graphGen.random_level(n, (7,10))

def fat_networks(n):
    return graphGen.random_level(10, (n,n))


constructors = [graph.Graph, graph.MatrixGraph]
generators = [tall_networks, fat_networks]
algorithms = [bg.busacker_gowen]

compareAlgorithms([bg.busacker_gowen], graph.Graph, tall_networks, meanMinMaxTiming).to_csv("test.csv")
print("Fin")