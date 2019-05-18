# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
    return True if a == b and len(a) == len(b) else False

assert is_permutation('Baba', 'Baba')
assert is_permutation('Baba ', 'Baba') # тут будет AssertionError
assert is_permutation('Baba ', 'baba')
assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')


"""
Эта часть просто вариация assert`ов выше.
baba -- это правильный образец
words -- список неправильных слов, которые сравниваются с 'baba' (см. выше)
err_counter -- +1 на каждой ошибке, на выходе сравниваем счетчик с кол-м ошибочных слов в списке.
"""

baba = 'Baba'
words = ['baba', 'abbba', 'abab', 'Baba ']
err_counter = 0

for i in range(len(words)):
    try:
        assert is_permutation(baba, words[i])
    except AssertionError:
        err_counter += 1
        continue

assert (False if (err_counter == len(words)) is True else True), "All words do not match with template."