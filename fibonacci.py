import time
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
def iterat(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



def recurs(n, memo=None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = recurs(n - 1, memo) + recurs(n - 2, memo)
    return memo[n]



N = 50

start = time.perf_counter()
iterat_result = iterat(N)
end = time.perf_counter()
logging.info(f"iterative fib({N}) = {iterat_result}")
logging.info(f"iterative time: {end - start:.6f} sec")

start = time.perf_counter()
recurs_result = recurs(N)
end = time.perf_counter()
logging.info(f"recursive fib({N}) = {recurs_result}")
logging.info(f"resursive time: {end - start:.6f} sec")