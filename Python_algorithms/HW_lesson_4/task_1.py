"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


numbers = [1, 3, 6, 9, 12, 15, 18]

print(timeit.repeat("func_1(numbers)", globals=globals(), repeat=3))


# Если изменить на генераторное выражение, получается приблизительно в 3 раза быстрее, так как он не хранит его в памяти
def func_2(nums):
    new_arr =(i for i in nums if i % 2 == 0)
    return new_arr


print(timeit.repeat("func_2(numbers)", globals=globals(), repeat=3))