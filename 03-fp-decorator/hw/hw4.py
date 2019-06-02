import os
from functools import wraps
from threading import Thread
from time import sleep, strftime
import random

storage = {}


def make_cache(seconds, key=None):
    def decorator(func):
        @wraps(func)
        def async_func(*args, **kwargs):
            nonlocal key
            th_func = Thread(target=func, args=args, kwargs=kwargs)
            storage.update([(key, th_func)])
            th_func.start()
            print(f'Function \'{func.__name__}\' was saved in storage for {seconds} seconds', storage)
            sleep(seconds)
            storage.pop(key)
            print(f'Function \'{func.__name__}\' was deleted from storage:', storage)
            return th_func
        return async_func
    return decorator


@make_cache(20, key=f'key{random.randint(0, 20)}')
def slow_function():
    with open(f'{os.getcwd()}\quotes.txt', encoding='utf-8') as f:
        quates = [q for q in f]
        index = random.randint(0, len(quates)-1)
        print(quates[index])
        print(f'Call storage from: {slow_function.__name__}', storage)

if __name__ == '__main__':

    def main():
        slow_function()
        print(f'BACK TO MAIN (time: {strftime("%H:%M:%S")})')

        slow_function()
        print(f'BACK TO MAIN (time: {strftime("%H:%M:%S")})')


    main()
