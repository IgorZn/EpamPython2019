"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

Вам нужны:
    1. Абстрактная фабрика с 3мя методами create_first, create_second, create_drink.
    2. Три конкретные фабрики, унаследованные от абстрактной и в них переопределена логика создания 1,2 и напитка
    3. Клиентский код, который принимает фабрику и вызывает у неё эти три метода
"""

import yaml
from datetime import date
import calendar

date = date.today()
weekday = calendar.day_name[date.weekday()]

with open('menu.yml', encoding='utf-8') as m:
    menu = yaml.safe_load(m)


class AbstractFactory(object):
    def create_first(self):
        raise NotImplementedError()

    def create_second(self):
        raise NotImplementedError()

    def create_drink(self):
        return NotImplementedError()


class ConcreteFactoryVegan1(AbstractFactory):
    _who = 'vegan'
    def create_first(self):
        return FirstVegan(menu[weekday]['first_courses'][self._who])

    def create_second(self):
        return SecondVegan(menu[weekday]['first_courses'][self._who])

    def create_drink(self):
        return DrinkVegan(menu[weekday]['first_courses'][self._who])


class ConcreteFactoryChild2(AbstractFactory):
    _who = 'child'
    def create_first(self):
        return FirstChild(menu[weekday]['first_courses'][self._who])

    def create_second(self):
        return SecondChild(menu[weekday]['second_courses'][self._who])

    def create_drink(self):
        return DrinkChild(menu[weekday]['drinks'][self._who])


class ConcreteFactoryChina3(AbstractFactory):
    _who = 'china'
    def create_first(self):
        return FirstChina(menu[weekday]['first_courses'][self._who])

    def create_second(self):
        return SecondChina(menu[weekday]['second_courses'][self._who])

    def create_drink(self):
        return DrinkChina(menu[weekday]['drinks'][self._who])


class AbstractFirst:
    def __init__(self, name):
        self._name = name
        print(self._name)

    def get_first(self):
        return NotImplementedError()


class AbstractSecond:
    def __init__(self, name):
        self._name = name
        print(self._name)

    def get_second(self):
        return NotImplementedError()


class AbstractDrink:
    def __init__(self, name):
        self._name = name
        print(self._name)

    def get_drink(self):
        return NotImplementedError()


class FirstChina(AbstractFirst):
    def get_first(self):
        print("First china dish")


class SecondChina(AbstractFirst):
    def get_second(self):
        print("Second china dish")


class DrinkChina(AbstractFirst):
    def get_drink(self):
        print("Drink china dish")


class FirstVegan(AbstractFirst):
    def get_first(self):
        print("First vegan dish")


class SecondVegan(AbstractFirst):
    def get_second(self):
        print("Second vegan dish")


class DrinkVegan(AbstractFirst):
    def get_drink(self):
        print("Drink vegan dish")


class FirstChild(AbstractFirst):
    def get_first(self):
        print("First child dish")


class SecondChild(AbstractFirst):
    def get_second(self):
        print("Second child dish")


class DrinkChild(AbstractFirst):
    def get_drink(self):
        print("Drink child dish")


factoryChina = ConcreteFactoryChina3().create_drink()
factoryChina.get_drink()

factoryVegan = ConcreteFactoryVegan1().create_drink()
factoryVegan.get_drink()

factoryChild = ConcreteFactoryChild2().create_drink()
factoryChild.get_drink()