from graph import Graph

def chaineAmeliorante(graph, startNode, endNode):
    q = [startNode]
    marking = set(startNode)

    while not (len(q) == 0 or endNode in marking):
        x = q.pop(0)

        for y, label in filter(lambda k: not k in marking, graph.getEdgesFrom(x)):
            _min, _max, cost, actual = label

            if actual < _max and not endNode in marking:
                marking.add(y)
                q.append(y)

        if not endNode in marking:
            for y, label in filter(lambda k: not k in marking, graph.getEdgesTo(x)):
                _min, _max, cost, actual = label

                if actual > _min:
                    marking.add(y)
                    q.append(y)

    if endNode in marking:
        return q
    else:
        return None

def arcAvantArriere(graph, chaineAmeliorante):
    arcs = [[_from, to] for _from, to in zip(chaineAmeliorante[:-1:], chaineAmeliorante[1::])]

    arcArriere = filter((lambda x: graph.getEdgeValue(x[0], x[1]) is None), arcs)
    arcAvant = filter((lambda x: not graph.getEdgeValue(x[0], x[1]) is None), arcs)

    return arcAvant, arcArriere

def augmentationFlots(graph, ca, arcAvant, arcArriere):
    deltaAv, deltaAr = None, None

    if len(arcAvant) > 0 and len(arcArriere) > 0:
        deltaAv = min([_max - actual for _min, _max, _cost, actual in map((lambda x: graph.getEdgeValue(x[0], x[1])), arcAvant)])
        deltaAr = min([actual - _min for _min, _max, _cost, actual in map((lambda x: graph.getEdgeValue(x[1], x[0])), arcArriere)])
    elif len(arcAvant) > 0:
        deltaAv = min([_max - actual for _min, _max, _cost, actual in map((lambda x: graph.getEdgeValue(x[0], x[1])), arcAvant)])
        deltaAr = deltaAv
    else:
        deltaAr = min([actual - _min for _min, _max, _cost, actual in map((lambda x: graph.getEdgeValue(x[1], x[0])), arcArriere)])
        deltaAv = deltaAr
        
    return min(lambdaAv, lambdaAr)

def fordFulkerson(graph, startNode, endNode):
    ca = chaineAmeliorante(graph, startNode, endNode)

    while ca != None:
        print "ok"
        arcAvant, arcArriere = arcAvantArriere(graph, ca)

        delta = augmentationFlots(graph, ca, arcAvant, arcArriere)

        for a in arcAvant:
            _min, _max, cost, actual = graph.getEdgeValue(a[0], a[1])

            graph.setEdgeValue(a[0], a[1], (_min, _max, cost, actual + delta))

        for a in arcArriere:
            _min, _max, cost, actual = graph.getEdgeValue(a[1], a[0])

            graph.setEdgeValue(a[1], a[0], (_min, _max, cost, actual - delta))

        ca = chaineAmeliorante(graph, startNode, endNode)




fordFulkerson.__setattr__("authors", ["Clement Derouet", "Christopher Vallot"])

flots = {
    "E": [("1", (0, 45, 0, 35)), ("2", (0, 25, 0, 25)), ("3", (0, 25, 0, 20))], 
    "1": [("a", (0, 10, 0, 10))], 
    "2": [("a", (0, 20, 0, 15))], 
    "1": [("b", (0, 15, 0, 5))], 
    "2": [("b", (0, 5, 0, 5))], 
    "2": [("c", (0, 5, 0, 5))], 
    "3": [("c", (0, 10, 0, 10))], 
    "1": [("d", (0, 20, 0, 20))], 
    "3": [("d", (0, 10, 0, 10))], 
    "a": [("S", (0, 30, 0, 25))],
    "b": [("S", (0, 10, 0, 10))], 
    "c": [("S", (0, 20, 0, 15))], 
    "d": [("S", (0, 30, 0, 30))],
    "S": []
}

g = Graph(flots)
print fordFulkerson(g, "E", "S")