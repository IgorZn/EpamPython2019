class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name} bark-bark!')


class Cat:
    def __init__(self, name):
        self.name = name

    def meaw(self):
        print(f'{self.name} meeeeeeaw!')


class Adapter(Dog):
    # благодаря адаптеру мы можем использовать
    # интерфейс класса `Dog`, а реализацию класса `Cat`.

    def __init__(self, name):
        super().__init__(name)
        self._cat = Cat(name)

    def bark(self):
        return self._cat.meaw()

dog = Dog('Тузик')
cat = Cat('Лепольд')

dog.bark()
cat.meaw()



dog = Adapter('Тузик')
dog.bark()