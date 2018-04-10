
import time
from pprint import pprint

def timeFunction(f, message=None):
    def intern(*args, **kwargs):
        before = time.time()
        result = f(*args, **kwargs)
        measured = time.time()-before
        if message:
            print("{} finished in {}".format(message, measured))
        return result, measured

    intern.__setattr__("authors", f.__dict__.get("authors"))
    intern.__setattr__("__name__", f.__name__)
    return intern

import pandas as pd

def runTests(constructors, generators, algorithms, testRepetition=100, sizes=[10, 20]):
    totalGenerationAmount = sum(map(lambda x: x*testRepetition, sizes))*len(generators)*len(constructors)
    print("Generating {} graphs...".format(totalGenerationAmount))


    timedAlgorithms = list(map(timeFunction, algorithms))

    def functionsTests(timedFunction, graphs):
        return list(map(lambda x: timedFunction(x, "E", "S"), graphs))

    testsData = {constructor.__name__: {size: {generator.__name__: {func.__name__: functionsTests(func,[constructor(generator(size)) for i in range(testRepetition)]) for func in timedAlgorithms }
                        for generator in generators}
                for size in sizes}
        for constructor in constructors }


    series = []
    for graphType, sizes in testsData.items():
        for size, generators in sizes.items():
            for generator, algorithms in generators.items():
                for (algorithm, v)  in algorithms.items():
                    for i,l in enumerate(zip(*v)):
                        if i == 0:
                            for j, r2 in enumerate(zip(*l)):
                                if j == 1:
                                    series.append(pd.Series([graphType, "size: {}".format(size), generator, algorithm, "flow"]+list(r2)))
                                elif j == 2:
                                    series.append(pd.Series([graphType, "size: {}".format(size), generator, algorithm, "cost"]+list(r2)))
                        else:
                            series.append(pd.Series([graphType, "size: {}".format(size), generator, algorithm, "timings"]+list(l)))


    df = pd.DataFrame(series)
    return df.T
    #pprint(testsData)

def meanMinMaxTiming(listOfResults):
    flows, costs, timings = list(map(list, zip(*map(lambda x: (x[0][1], x[0][2], x[1]), listOfResults))))
    returned = {}

    returned["meanflow"] = sum(flows)/ len(flows)
    returned["meanCost"] = sum(costs)/ len(costs)
    returned["meanTime (s)"] = sum(timings)/ len(timings)

    return returned


def testAlgorithm(algorithm, constructor, generator, evaluator, sizes=[5,10],  repetition=5):

    graphData = {graphSize: [constructor(generator(graphSize)) for i in range(repetition)] for graphSize in sizes}

    evaluated_data = {}

    timedAlgorithm = timeFunction(algorithm)

    for size, graphList in graphData.items():
        evaluated = evaluator([timedAlgorithm(graph, "E", "S") for graph in graphList])
        evaluated_data[size] = evaluated

    #pprint(evaluated_data)

    #s = pd.Series(evaluated_data, name=algorithm.__name__)

    return evaluated_data

def compareAlgorithms(algorithms, constructor, generator, evaluator, sizes=[5, 10], repetition=5):

    result = {algorithm.__name__ : pd.DataFrame(testAlgorithm(algorithm, constructor, generator, evaluator, sizes, repetition)) for algorithm in algorithms}


    df = pd.concat(result, axis=1)

    return df

