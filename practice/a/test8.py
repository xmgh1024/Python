class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender','_jiguan')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

    def __str__(self):
        return str(self._age) + self._name


def main():
    person = Person('王大锤', 22)
    print(person)
    person.play()
    person.age = 12
    print(person)
    person._age = 13
    print(person)
    person._gender = '男'
    print(person._gender)
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True
    person._jiguan = '北京'


if __name__ == '__main__':
    main()
