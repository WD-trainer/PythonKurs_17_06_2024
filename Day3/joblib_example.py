from math import sqrt
from functools import wraps
from time import time


from joblib import Parallel, delayed # pip install joblib

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

@timing
def single_thread():
    calculating = [sqrt(i ** 2) for i in range(10000)]
    return calculating


@timing
def multithreading():
    calculating_parallel = Parallel(n_jobs=10)(delayed(sqrt)(i ** 2) for i in range(10000))
    return calculating_parallel

print(single_thread())
print(multithreading())