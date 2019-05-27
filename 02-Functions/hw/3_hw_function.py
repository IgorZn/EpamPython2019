counter_name = 1

def tester():
    print('Im tester func',)

def make_it_count(func, glb_var):
    def new_func(func):
        global counter_name
        print(counter_name, 'original value')
        func()
        counter_name += 1
        print(counter_name, 'new value')

    return new_func(func)

make_it_count(tester, counter_name)