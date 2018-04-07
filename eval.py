
import time


def timeFunction(f):
    def intern(*args, **kwargs):
        before = time.time()
        result = f(*args, **kwargs)
        return result, time.time()-before
    return intern

def test():
    return 1


test.__setattr__("authors", ["Ben"])

print(test.authors)

class TestFramework:
    def __init__(self, generators, algorithms, testRepetition=100, sizes=[10,100,1000]):
        pass