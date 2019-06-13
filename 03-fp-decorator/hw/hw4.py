import os
import time
from functools import wraps
from time import sleep, strftime
import random

storage = {}


def make_cache(seconds, *args, **kwargs):
    def decorator(func):
        @wraps(func)
        def async_func(*args, **kwargs):
            current_time = time.time()
            result = func(*args, **kwargs)
            storage.update([(current_time, func)])
            s = storage.copy()  # to avoid “RuntimeError: dictionary changed size during iteration”
            for key in s.keys():
                if current_time - key > seconds:
                    storage.pop(key)
            return result
        return async_func
    return decorator


@make_cache(20)
def slow_function():
    with open(f'{os.getcwd()}\quotes.txt', encoding='utf-8') as f:
        quates = [q for q in f]
        index = random.randint(0, len(quates)-1)
        print(quates[index])
        sleep(10)


if __name__ == '__main__':

    def main():
        for i in range(5):
            slow_function()
            print(storage.keys())


    main()
