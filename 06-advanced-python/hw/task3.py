"""
Реализовать дескриптор, кодирующий слова с помощью шифра Цезаря

"""
import string

class ShiftDescriptor:

    def __init__(self, shift):
        self.shift = shift
        self.value = ''

    def __get__(self, instance, owner):
        """
        берет значение атрибута у родительского класс
        :param instance:
        :param owner:
        :return:
        """
        return self.value

    def __set__(self, instance, value):
        """
        устанавливает значение атрибута родительского класса
        :param instance:
        :param value:
        :return:
        """
        self.value = self.output_string(value, self.shift)
        return

    def output_string(self, value, shift):
        out = ''
        caesar = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
        normal = string.ascii_lowercase
        for x in value:
            out += caesar[normal.index(x)]
        return out

class CeasarSipher:

    message = ShiftDescriptor(4)
    another_message = ShiftDescriptor(7)


a = CeasarSipher()
a.message = 'abc'
a.another_message = 'hello'

assert a.message == 'efg'
assert a.another_message == 'olssv'