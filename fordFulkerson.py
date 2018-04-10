from graph import Graph

def fordFulkerson(graph, startNode, endNode):
    marking = {}
    maxEdges = {}

    for _from, to, label in graph.getAllEdges():
        _min, _max, cost = label
        maxEdges[(_from, to)] = _max
        marking[(_from, to)] = 0


    def fordFulkersonRec(_max, prevNode, currentNode):
        prevEdge = (prevNode, currentNode)

        if currentNode != endNode:
            for nextNode, label in graph.getEdgesFrom(currentNode):
                nextEdge = (currentNode, nextNode)
                originalNextMarking = marking[nextEdge]

                _max = min(maxEdges[prevEdge] - marking[prevEdge], maxEdges[nextEdge] - marking[nextEdge])

                fordFulkersonRec(_max, currentNode, nextNode)

                marking[prevEdge] += marking[nextEdge] - originalNextMarking
        else:
            marking[prevEdge] += _max

    for nextNode, label in graph.getEdgesFrom(startNode):
        fordFulkersonRec(label, startNode, nextNode)

    return sum([marking[(startNode, nextNode)] for nextNode, label in graph.getEdgesFrom(startNode)])


fordFulkerson.__setattr__("authors", ["Clement Derouet", "Christopher Vallot"])