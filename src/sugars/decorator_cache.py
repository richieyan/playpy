"""
https://stackoverflow.com/questions/7492068/python-class-decorator-arguments
http://scottlobdell.me/2015/04/decorators-arguments-python/

@Cache
def double(...): 
   ...
is equivalent to

def double(...):
   ...
double=Cache(double)
While

@Cache(max_hits=100, timeout=50)
def double(...):
   ...
is equivalent to

def double(...):
    ...
double = Cache(max_hits=100, timeout=50)(double)
"""
class _Cache(object):
    def __init__(self, function, max_hits=10, timeout=5):
        self.function = function
        self.max_hits = max_hits
        self.timeout = timeout
        self.cache = {}
        self.lastArgs = None

    def __call__(self, *args):
        if self.lastArgs and self.lastArgs == args:
            print 'from cache'
            return self.cache[id(self.lastArgs)]
        value = self.function(*args)
        self.lastArgs = args
        self.cache[id(self.lastArgs)] = value
        return value

# wrap _Cache to allow for deferred calling
def Cache(function=None, max_hits=10, timeout=5):
    if function:
        return _Cache(function)
    else:
        def wrapper(function):
            return _Cache(function, max_hits, timeout)

        return wrapper

@Cache
def double(x):
    print 'double'
    return x * 2

@Cache(max_hits=100, timeout=50)
def doublex(x):
    print 'doublex'
    return x * 2

if __name__ == '__main__':
    double(10)
    double(10)
    doublex(9)
    doublex(9)
    doublex(7)
    doublex(9)