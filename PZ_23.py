"""
Написать функцию get_indexes которая принимает два списка и возвращает список индексов, в которых элемент из первого
списка меньше элемента из второго списка по данному индексу. Желательно проходиться сразу по двум массивам одновременно
(вспомните функцию zip). Для нахождения индексов можно использовать enumerate вместе с zip.
"""


from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    result = [i for i, (num1, num2) in enumerate(zip(nums1, nums2)) if num1 < num2]
    return result


code = []
while data := input():
    data = data.replace('\xa0', '   ')
    code.append(data)
code = "\n".join(code)
exec(code)
