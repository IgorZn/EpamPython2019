"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseCoffe(Component):
    def get_cost(self):
        return 90

class Whip:
    def __init__(self, coffe):
        self._coffe = coffe

    def __getattr__(self, item):
        return getattr(self._coffe, item)

    def add_whip_cream(self):
        print('Whip cream has been added.')

    def get_cost(self):
        return self._coffe.get_cost() + 10


class Marshmallow:
    def __init__(self, coffe):
        self._coffe = coffe

    def __getattr__(self, item):
        return getattr(self._coffe, item)

    def add_marshmallow(self):
        print('Marshmallow has been added.')

    def get_cost(self):
        return self._coffe.get_cost() + 10

class Syrup:
    def __init__(self, coffe):
        self._coffe = coffe

    def __getattr__(self, item):
        return getattr(self._coffe, item)

    def add_syrup(self):
        print('Syrup has been added.')

    def get_cost(self):
        return self._coffe.get_cost() + 10

if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))

