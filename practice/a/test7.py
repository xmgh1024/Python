# 自定义类
class Person(object):
    def __init__(self, age, name):
        self._age = age
        self._name = name

        # 访问器 - getter方法

    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def __str__(self):
        return str(self._age)+self._name

def main():
    person = Person(18, "xiaoxiao")
    print(person.age,person.name)
    name = person.name
    print(name)
    person.age=12
    print(person)


if __name__ == '__main__':
    main()
