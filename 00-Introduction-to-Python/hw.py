# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
    if len(a) == len(b) and sorted(a) == sorted(b):
        return True
    return False

assert is_permutation('Baba', 'Baba')
assert is_permutation('Baba ', 'baba')
assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
assert is_permutation('Baba ', 'Baba')