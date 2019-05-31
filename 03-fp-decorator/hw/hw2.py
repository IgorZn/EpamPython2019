def is_armstrong(number):
    length = int(len(f"{number}"))
    digit = [x for x in map(int, f"{number}")]
    return True if number == sum([x**length for x in digit]) else False


print(list(filter(is_armstrong, [153, 9, 10, 333, 370, 371, 407])))