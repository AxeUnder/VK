"""
Напишите декоратор, который будет принимать натуральное число n – число повторений –
и будет повторять вызов декорированной функции n раз, а также возвращать значение
из последнего вызова. Дополните код ниже, дописав свой код в секции “YOUR CODE HERE”.
"""


def repeat_deco(n=1):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return inner
    return wrapper


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
