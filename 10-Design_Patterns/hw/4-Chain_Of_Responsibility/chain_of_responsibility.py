"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""


class Eggs:
    def handle(self, count):
        if count == 2:
            return "Яйцо отборное кат. С0, в количестве ДВУХ шт. готовы стать частью блинов!"

    def err(self):
        print(f'Нехватает {__class__.__name__}')


class Flour:
    def handle(self, count):
        if count == 300:
            return "300 муки есть!"

    def err(self):
        print(f'Нехватает {__class__.__name__}')


class Milk:
    def handle(self, count):
        if count == 500:
            return "500 мл молочка есть!"

    def err(self):
        print(f'Нехватает {__class__.__name__}')


class Sugar:
    def handle(self, count):
        if count == 100:
            return "100 сахарку в ниличие!"

    def err(self):
        print(f'Нехватает {__class__.__name__}')


class SunOil:
    def handle(self, count):
        if count == 10:
            return "10 мл подсолнечного масла есть."
        else:
            print(f'Нехватает {__class__.__name__}')


class Butter:
    def handle(self, count):
        if count == 10:
            return "10 гр масла есть."

    def err(self):
        print(f'Нехватает {__class__.__name__}')


class Blin:
    def __init__(self):
        self.elements = []

    def add_elements(self, element):
        self.elements.append(element)

    def make_a_blin(self, ingredient):
        for element in self.elements:
            msg = element.handle(ingredient)
            if msg:
                print(msg)
                break



ingredients = {
        'eggs': 2,
        'flour': 300,
        'milk': 500,
        'sugar': 100,
        'sun_oil': 10,
        'butter': 120
    }

eggs = Eggs()
flour = Flour()
milk = Milk()
sugar = Sugar()
sun_oil = SunOil()
butter = Butter()
blin = Blin()

handlers = [eggs, flour, milk, sugar, sun_oil, butter]

for handler in handlers:
    blin.add_elements(handler)

for ingredient in ingredients:
    blin.make_a_blin(ingredients[ingredient])
