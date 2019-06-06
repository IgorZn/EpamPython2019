import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):
    def new_func(*fixed_args, **fixed_kwargs):
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[3]
        code = inspect.getsource(func)
        if len(args['fixated_args']) == 0 and len(args['fixated_kwargs']) == 0:
            print(len(args['fixated_args']), len(args['fixated_kwargs']))
            return func(*fixated_args, **fixated_kwargs)

        doc = f"A func implementation of {func.__name__} \nwith pre-applied arguments being: fixated_args: {str(args['fixated_args'])} \nfixated_kwargs: {str(args['fixated_kwargs'])}, \nsource_code: \n{code}"
        new_func.__doc__ = doc
        new_func.__name__ = f'func_{func.__name__}'
        sum_args = [*fixated_args, *fixed_args]
        sum_kwargs = {**fixated_kwargs, **fixed_kwargs}
        return func(*sum_args, **sum_kwargs)
    return new_func

def foo(*args, **kwargs):
    """
    just foo
    :param args:
    :param kwargs:
    :return:
    """
    print('Hello world')

gg = modified_func(foo)
hh = modified_func(foo, 'j')
gg()
hh()
print(gg.__doc__, gg.__name__)
print(hh.__doc__, hh.__name__)