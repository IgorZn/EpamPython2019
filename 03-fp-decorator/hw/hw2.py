def is_armstrong(number):
    return True if number == sum([x**int(len(f"{number}")) for x in [x for x in map(int, f"{number}")]]) else False


print(list(filter(is_armstrong, [153, 9, 10, 333, 370, 371, 407])))