import os
import sys
import time
from functools import wraps

def make_cache(second):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(second)
            return result
        return wrapper
    return decorator

@make_cache(30)
def slow_function():
    """
    shutdown PC if you really want.
    :return:
    """
    if sys.platform == 'win32':
        os.popen('shutdown.exe /f /s /t 30').read()
        inp = input('Cancel shutdown? [yes/no]').lower()
        if inp.startswith('yes'):
            os.popen('shutdown.exe /a').read()
    else:
        os.popen('shutdown.exe -P -t 30').read()
        inp = input('Cancel shutdown? [yes/no]').lower()
        if inp.startswith('yes'):
            os.popen('shutdown.exe -c').read()



slow_function()