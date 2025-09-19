# Лабораторная работа 1
"""
Дан массив целых чисел nums и целочисленное значение переменной target,
верните индексы двух чисел таким образом, чтобы они в сумме давали target.
У каждого входного набора может не быть решений/быть только одно решение,
если есть элементы дающие в сумме target. Нельзя использовать один и тот же элемент дважды (и соответственно индекс тоже).
"""


def f(nums, target):
    if len(nums) < 2:
        return None

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


target = int(input('Введите target: '))
nums = list(map(int, input('Введите элементы через пробел: ').split()))
print('Вывод: ', f(nums, target))
