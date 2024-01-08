"""
Представьте, что у вас есть словарь с ключами и их частотами (то есть насколько часто встречался каждый ключ)
в качестве значений. Напишите функцию make_most_common_keys, которая принимает словарь частот и выводит отсортированный
(например через функцию sorted) по убыванию частот (то есть значений ключей) список ключей.
"""

from typing import List, Dict, Type


def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    sort_d = []
    for k, hz in sorted(d.items(), key=lambda item: item[1], reverse=True):
        sort_d.append(k)
    return sort_d


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
