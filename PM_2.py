"""
Необходимо написать генераторную функцию solution, которая будет фильтровать данные из последовательности data функцией
func_filter, к полученным данным применять функцию func_map и возвращать в качестве значения каждый второй элемент
полученной последовательности. Нужно пользоваться здесь концепцией генератора, то есть обрабатывать не все данные разом,
а только те, что необходимы для возвращения следующего значения. Дополните также код своей реализацией кэшируещего
декоратора.
"""


def cache_deco(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper


@cache_deco
def solution(func_map, func_filter, data):
    counter = 0
    for item in data:
        if func_filter(item):
            mapped_item = func_map(item)
            if counter % 2 == 0:
                yield mapped_item
            counter += 1


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
