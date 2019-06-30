class Man(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f'Hello, my name is {self.name}!')


class ExtaOption(object):
    def __init__(self, man):
        self.man = man

    def __getattr__(self, item):
        return getattr(self.man, item)

    def take_cola(self):
        print(f"{self.man.name} wants coca-cola!")

man = Man('Putin')
man_extra = ExtaOption(man)

man_extra.say()
man_extra.take_cola()

