"""
Реализовать метод calculate_period с декоратором classmethod в классе “Pendulum”, в котором написаны два атрибута класса:
    g =10
    pi = 3.14
Этот метод должен вычислять период математического маятника по формуле:
T=2π√l/g
"""

import math


class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        T = 2 * cls.pi * (length / cls.g) ** 0.5
        return T


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
