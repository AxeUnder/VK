"""
Напишите декоратор, который будет кэшировать вызовы функции, которая будет передана на вход. То есть декоратор должен
проверить нет ли в кэше (например, словаре) значения, и если нет, то вычислить и запомнить результат, если есть,
то взять это значение.
"""


def cache_deco(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)