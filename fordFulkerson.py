from queue import Queue
import busacker_gowen as bg


def chaineAmeliorante(flow, startNode, endNode):
    q = []
    marking = set()

    ret = [startNode]

    marking.add(startNode)
    q.append(startNode)

    cond = True
    while cond:
        x = q.pop(0)
        addNode = True
        for y, label in filter(lambda k: k[0] not in marking, flow.getEdgesFrom(x)):
            _min, _max, cost, actual = label

            if actual < _max:
                if addNode and x == ret[-1]:
                    ret.append(y)
                    addNode = False
                marking.add(y)
                q.append(y)

        for y, label in filter(lambda k: k[0] not in marking, flow.getEdgesTo(x)):
            _min, _max, cost, actual = label

            if actual > _min:
                marking.add(y)
                q.append(y)
        cond = len(q) > 0 and endNode not in marking
    if ret[-1] == endNode:
        return ret
    else:
        return []

def fordFulkerson(graph, starting, ending):
    return chaineAmeliorante(bg.getFlotNul(graph), starting, ending)

fordFulkerson.__setattr__("authors", ["Clement Derouet", "Christopher Vallot"])