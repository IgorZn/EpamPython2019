import string

def letters_range(*args, **kwargs):
    # no args, no work
    if len(args) == 0:
        raise Exception('letters_range expected at least 1 arguments, got 0')

    # default values for start and step
    start = 0
    step = 1
    stop = string.ascii_lowercase.index(args[0])
    letters = [l for l in string.ascii_lowercase]

    if kwargs:
        for key in kwargs:
            i = letters[key]
            letters[i] = kwargs[key]

    # just 'stop'
    if len(args) == 1:
        print(letters[start:stop:step])

    # stop and start
    if len(args) == 2:
        start = string.ascii_lowercase.index(args[0])
        stop = string.ascii_lowercase.index(args[1])
        print(letters[start:stop:step])

    # start, stop and step
    if len(args) == 3:
        start = string.ascii_lowercase.index(args[0])
        stop = string.ascii_lowercase.index(args[1])
        step = args[2]
        print(letters[start:stop:step])


letters_range('b', 'w', 2)
# ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v']

letters_range('g')
# ['a', 'b', 'c', 'd', 'e', 'f']

letters_range('g', 'p')
# ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

letters_range('g', 'p', **{'l': 7, 'o': 0})
# ['g', 'h', 'i', 'j', 'k', 700, 'm', 'n', 0]p

letters_range('p', 'g', -2)
# ['p', 'n', 'l', 'j', 'h']

letters_range('a')
# []
