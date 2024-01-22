"""
Реализуйте 3 метода в классе “Person”:
    __init__(self, age), в котором будет объявляться атрибут возраста
    age с декоратором property, который будет возвращать атрибут возраста
    age с декоратором age.setter
    Этот метод должен обрабатывать изменение проперти “age”: при передаче значений < 0 атрибут возраста = 0, в противном
    случае атрибут возраста будет равен тому значению, которое передано
"""


class Person:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0
        else:
            self._age = value


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
