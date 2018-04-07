
import time
from pprint import pprint

def timeFunction(f):
    def intern(*args, **kwargs):
        before = time.time()
        result = f(*args, **kwargs)
        return result, time.time()-before
    return intern

def test():
    return 1


test.__setattr__("authors", ["Ben"])

def runTests(constructors, generators, algorithms, testRepetition=100, sizes=[10,100,1000]):
    testsData = [ [ [ (generator.__name__, [constructor(generator(size)) for i in range(testRepetition)])
                      for generator in generators] for size in sizes] for constructor in constructors]

    pprint(testsData)




runTests([lambda x: x], [lambda x: x], 0)
