"""
Реализуйте метод calculate_area в классе “Circle”, в котором уже есть атрибут класса pi, который понадобится для
расчета:
Этот метод будет рассчитывать площадь круга по формуле S=πR^2, где R передается в качестве параметра
"""


class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        S = self.pi * radius * radius
        return S


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
