"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import time


def decorator(func):
    def tags(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Время работы функции {func.__name__}:  {time.time()-start}")

        return result
    return tags


@decorator
def list_1():
    return  [i for i in range(5000000)]


@decorator
def dict_1():
    return {i: f"{i}" for i in range(5000000)}


dict_1 = dict_1()
list_1 = list_1()

"""
Вывод: По моим наблюдениям, запись нового элемента в словарь происходит медленней, пототому что сначала он считает хэш,
и только потом кладёт в память. В списке же запись происходит сразу в выделенную память.
"""

@decorator
def change_dict(dict_1):
    for i in dict_1:
        if i % 2 == 0:
            dict_1[i] = "GeekBrains"
    return dict_1

@decorator
def change_list(list_1):
    for i in range(len(list_1)):
        if i % 2 == 0:
            list_1[i] = "GeekBrains"
    return list_1

change_dict(dict_1)
change_dict(list_1)

"""
Вывод: Я заметил что замена элемента проходит +-одинаково, по весу алгоритма O(n). 
Но если элемент известен, то словарь справиться быстрее, и решение будет константой O(1)
"""

@decorator
def del_elem_dict(dict_1):
    num = 999999
    del dict_1[num]

@decorator
def del_elem_list(list_1):
    num = 999999
    del list_1[num]

print(del_elem_dict(dict_1))
print(del_elem_list(list_1))

"""
Вывод: Получается что удаление в словаре N элемента происходит быстрее т.к. вес алгоритма = константе, O(1).
 А из списка алгоритм имеев вес линейной сложности O(n), соответственно тяжелее.
"""