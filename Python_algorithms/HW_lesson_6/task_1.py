"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from random import randint
from memory_profiler import memory_usage
from timeit import default_timer


def decoration(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Использовано памяти: {memory_usage()[0] - memory[0]}')
        print(f'Использовано времени: {default_timer() - start}')
        return result

    return wrapper


# Первый пример: сравнение генератора и списка
@decoration
def my_func():
    my_list = (i for i in range(999999))
    yield my_list


@decoration
def my_func2():
    my_list = [i for i in range(999999)]
    return my_list


my_func()
my_func2()

'''
Здесь мы сравниваем работу генератора и создание списка. Генератор тратит меньше памяти, т.к. 
не хранит целый список, а выдаёт элементы по запросам.
'''


# Второй пример: сравнение работы списка, и встроенной функции map
@decoration
def my_func3():
    my_list = [i for i in range(9999999)]
    new_list = [i ** 2 for i in my_list]
    return new_list


@decoration
def my_func4():
    my_list = [i for i in range(9999999)]
    new_list = map(lambda i: i ** 2, my_list)
    return new_list


'''
Как мы видим из результатов, функция map использует гораздо меньше памяти, и экономит время более чем в несколько раз.
'''

my_func3()
my_func4()
