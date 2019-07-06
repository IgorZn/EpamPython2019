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

# print(menu)

class AbstractFactory:
    def get_lunch(self):
        raise NotImplementedError()


class Monday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Tuesday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Wednesday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Thursday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Friday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Saturday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink

class Sunday:
    def __init__(self, type, for_whom, drink):
        self._menu = menu
        self._lunch = self._menu[self.__class__.__name__][type][for_whom]
        self._drink = self._menu[self.__class__.__name__]['drinks'][drink]

    def __str__(self):
        return '\n\t' + self._lunch + '. ' + self._drink


class LunchFactory(AbstractFactory):
    def get_lunch(self):
        print(f'Today is {weekday} and we have two set lunchs: first, second and drinks, dishes: for vegan, child and china')
        number = int(input('Select first or second set lunch. Type 1 or 2: '))-1
        for_whom = input('Type of food vegan, child or china. Type vegan, child or china: ')
        drink = input('Drinks for vegan, child or china. Type vegan, child or china: ')

        menus = ['first_courses', 'second_courses']


        if weekday == 'Monday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Tuesday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Wednesday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Thursday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Friday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Saturday':
            return Saturday(menus[number], for_whom, drink)

        if weekday == 'Sunday':
            return Saturday(menus[number], for_whom, drink)


if __name__ == '__main__':
    factory = LunchFactory()
    print(f'\nСегодня {weekday}\nА вот и ваш обед:', factory.get_lunch())





