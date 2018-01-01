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

参数方式多了一次调用，必须使用有()

"""
import functools

class Cache(object):
    def __init__(self, max_hits=10, timeout=5):
        print("cache __init__")
        self.max_hits = max_hits
        self.timeout = timeout
        self.cache = {}
        self.lastArgs = None

    def __call__(self, fn):
        print('wraps--->',fn)
        @functools.wraps(fn)
        def decorated(*args,**kwargs):
            if self.lastArgs and self.lastArgs == args:
                print 'from cache'
                return self.cache[id(self.lastArgs)]
            value = fn(*args)
            self.lastArgs = args
            self.cache[id(self.lastArgs)] = value
        return decorated


@Cache(max_hits=100, timeout=50)
def doublex(x):
    print 'doublex'
    return x * 2

print("start cache")
@Cache() #使用参数的方式，必须调用一次
def double(x):
    print 'double'
    return x * 2


if __name__ == '__main__':
    double(10)
    double(10)
    doublex(9)
    doublex(9)
    doublex(7)
    doublex(9)