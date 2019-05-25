import string

def letters_range(*args):
    # default values for start and step
    start = 0
    step = 1

    # no args, no money
    if len(args) == 0:
        raise TypeError('stop value is not present.')

    # single args, use as 'stop'
    elif len(args) == 1:
        stop = string.ascii_lowercase.index(args[0])
        letters = [letter for letter in string.ascii_lowercase[start:stop:step]]
        print(letters)

    elif len(args) == 2:
        start = string.ascii_lowercase.index(args[0])
        stop = string.ascii_lowercase.index(args[1])
        letters = [letter for letter in string.ascii_lowercase[start:stop:step]]
        print(letters)

    elif len(args) == 3:
        start = string.ascii_lowercase.index(args[0])
        step = args[2]
        stop = string.ascii_lowercase.index(args[1])
        letters = [letter for letter in string.ascii_lowercase[start:stop:step]]
        print(letters)


letters_range('b', 'w', 2)
letters_range('g')
letters_range('g', 'p')
letters_range('p', 'g', -2)
letters_range('a')
# letters_range('g', 'p', **{'l': 7, 'o': 0})
