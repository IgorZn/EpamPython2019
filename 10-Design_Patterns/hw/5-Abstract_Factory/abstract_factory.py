"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""
from datetime import date
import calendar
import yaml

date = date.today()
weekday = calendar.day_name[date.weekday()]

with open('menu.yml', encoding='utf-8') as m:
    menu = yaml.safe_load(m)


class AbstractFactory:
    def get_lunch(self):
        raise NotImplementedError()


class Monday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Tuesday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Wednesday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Thursday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Friday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Saturday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch

class Sunday:
    def __init__(self, type, for_whom):
        self._menu = menu
        self._lunch = self._menu[super().__class__.__name__][type][for_whom]

    def __str__(self):
        return self._lunch


class LunchFactory(AbstractFactory):
    def get_lunch(self):
        print(f'Today is {weekday} and we have two set lunchs: first, second and drinks, dishes: for vegan, child and china')
        number = input('Select first or second set lunch: ')
        for_whom = input('Type of food vegan, child or china: ')
        drinks = input('Drinks for vegan, child or china: ')

        if weekday == 'Monday':
            return Monday('Hamburger')
        if weekday == 'Tuesday':
            return Monday('Hamburger')
        if weekday == 'Wednesday':
            return Monday('Hamburger')
        if weekday == 'Thursday':
            return Monday('Hamburger')
        if weekday == 'Friday':
            return Monday('Hamburger')
        if weekday == 'Saturday':
            return Monday('Hamburger')
        if weekday == 'Sunday':
            return Monday('Hamburger')


if __name__ == '__main__':





    print(factory.create_drink())   # Pepsi
    print(factory.create_food())    # Cheeseburger