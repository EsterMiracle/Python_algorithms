"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile
def my_func(number):
    def count(number):
        if number <= 1:
            return number
        return count(number - 1) + count(number - 2)
    return print(count(number))


'''
Если производить замеры обычным методом, мы получаем таблицу на каждый вызов функции.
Но если обернуть рекурсивную функцию в обычную,
то как мы видим декоратор выполняется только на обычную функцию, не вызываясь рекурсивно.
'''