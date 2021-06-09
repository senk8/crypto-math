from functools import wraps
import time

def time_measurement(func):
    @wraps(func)
    def inner(*args,**kargs):

        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start

        print(f"{elapsed_time} ms in {func.__name__}")
        return result
    return inner
