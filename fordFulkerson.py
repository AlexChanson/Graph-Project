from queue import Queue

def fordFulkerson(flow, startNode, endNode):
    q = Queue()
    marking = set()

    marking.add(startNode)
    q.put(startNode)

    while not (q.empty() or endNode in marking):
        x = q.get()

        for y, label in filter(lambda k: not k in marking, flow.getEdgesFrom(x)):
            _min, _max, cost = label

            if cost < _max and not endNode in marking:
                marking.add(y)
                q.put(y)

        if not endNode in marking:
            for y, label in filter(lambda k: not k in marking, flow.getEdgesTo(x)):
                _min, _max, cost = label

                if cost > _min:
                    marking.add(y)
                    q.put(y)

    if endNode in marking:
        ret = None
        y = q.get()

        while y != startNode:
            y = q.get()

        while y != endNode:
            if y == startNode:
                ret = Queue()

            ret.put(y)

            y = q.get()

        ret.put(endNode)

        return ret
    else:
        return None

fordFulkerson.__setattr__("authors", ["Clement Derouet", "Christopher Vallot"])