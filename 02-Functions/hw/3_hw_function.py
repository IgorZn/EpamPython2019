a = 1

def tester():
    print('Im tester func',)

def make_it_count(func, glb_var):
    def new_func(func):
        global a
        print(a, 'original value')
        func()
        a += 1
        print(a, 'new value')

    return new_func(func)

make_it_count(tester, a)