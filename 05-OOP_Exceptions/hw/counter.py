"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""
    setattr(cls, 'counter', 0)

    def __init__(self):
        cls.counter += 1

    def get_created_instances(self=None) -> int:
        """
        возвращает количество созданых экземпляров класса
        :param self:
        :return: int
        """
        print(cls.counter)
        return cls.counter

    def reset_instances_counter(self=None) -> int:
        """
        сбросить счетчик экземпляров, возвращает значение до сброса
        :param self:
        :return: int
        """
        tmp_cnt = cls.counter
        setattr(cls, 'counter', 0)
        print(tmp_cnt)
        return tmp_cnt

    methods = [__init__, get_created_instances, reset_instances_counter]

    # add methods to class
    for method in methods:
        setattr(cls, method.__name__, method)

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
