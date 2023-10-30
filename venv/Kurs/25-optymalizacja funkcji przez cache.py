from datetime import datetime as dt
import time
import functools
@functools.lru_cache(100)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result
start = time.time()

start = time.time()
for i in range(334):
    result = fib(i)
    print('{0:2d}  {1}, time = {2:3.2f}'.format(i, result, time.time() - start))

print(fib.cache_info())

