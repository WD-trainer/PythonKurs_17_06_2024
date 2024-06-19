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


# def calculate_sum(data: list[int], start: int, end: int, result: list[int]):
#     partial_sum = sum(data[start:end])
#     result.append(partial_sum)
#
#
# def main_threading():
#     data = list(range(1000000))
#     num_threads = 4
#     chunk_size = len(data) // num_threads
#
#     result = []
#     threads = []
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = start + chunk_size if i < num_threads - 1 else len(data)
#         thread = threading.Thread(target=calculate_sum, args=(data, start, end, result))
#         thread.start()
#         threads.append(thread)
#
#     for thread in threads:
#         thread.join()
#
#     total_sum = sum(result)
#     print("Total sum:", total_sum)

def calculate_sum(data_chunk):
    return sum(data_chunk)

data = list(range(1000000))
num_threads = 4
chunk_size = len(data) // num_threads

chunks = [data[i * chunk_size: (i+1) * chunk_size] for i in range(num_threads)]
results = Parallel(n_jobs=num_threads)(delayed(calculate_sum)(chunk) for chunk in chunks)

total_sum = sum(results)