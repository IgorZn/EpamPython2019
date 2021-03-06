def atom(a, *args):

    if a:
        def get_value():
            print('get_value ->', a)
            return a

        def set_value():
            nonlocal a
            a += 1
            print('set_value ->', a)
            return a

        def process_value(*args):
            nonlocal a
            for x in range(len(args)):
                a += args[x](a)
            print('process_value ->', a)

        def delete_value():
            nonlocal a
            del a

        return get_value(), set_value(), process_value(*args), delete_value()


def f1(a):
    b = a + 1
    return b

def f2(a):
    b = a + 2
    return b

def f3(a):
    b = a + 3
    return b


atom(1, f1, f2, f3)