"""
В классе Dictionary реализуйте методы __call__ и __init__:
В __init__(self, dictionary) объявите словарь в качестве атрибута
В методе call реализуйте поиск в словаре по ключу
"""


class Dictionary:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __call__(self, key):
        return self.dictionary[key]


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
