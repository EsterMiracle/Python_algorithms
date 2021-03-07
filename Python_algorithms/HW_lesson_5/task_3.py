"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям
И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit

my_list = [el for el in range(100000)]
my_deque = deque(my_list)
some_elem = True
some_list = [1, 2]


def append_in_list(check_list, el):
    check_list.insert(0, el)


def append_in_deque(check_deque, el):
    check_deque.appendleft(el)


print("append list")
print(timeit("append_in_list(my_list, some_elem)", globals=globals(), number=10000))
print("append deque")
print(timeit("append_in_deque(my_deque, some_elem)", globals=globals(), number=10000))


def pop_in_list(check_list):
    check_list.pop(0)


def pop_in_deque(check_deque):
    check_deque.popleft()


print("pop list")
print(timeit("pop_in_list(my_list)", globals=globals(), number=10000))
print("pop deque")
print(timeit("pop_in_deque(my_deque)", globals=globals(), number=10000))


def extend_in_list(check_list, el):
    for i in el:
        check_list.insert(0, i)


def extend_in_deque(check_deque, el):
    check_deque.extendleft(el)


print("extend list")
print(timeit("extend_in_list(my_list, some_list)", globals=globals(), number=10000))
print("extend deque")
print(timeit("extend_in_deque(my_deque, some_list)", globals=globals(), number=10000))


def pop_list(check_list):
    check_list.pop()


def pop_deque(check_deque):
    check_deque.pop()


print('pop list')
print(timeit('pop_list(my_list)', globals=globals(), number=10000))
print('pop deque')
print(timeit('pop_deque(my_deque)', globals=globals(), number=10000))

"""
Вывод:
Анализируя расчёты, мы видим что встроенные в deque операции работают быстрее, чем при таких же условиях в списках.
Это связанно с тем, что deque добавляет и убирает элементы со сложностью алгоритма О(1), а список переопределяет ссылки
на элементы со сложностью алгоритма с О(n)
"""
