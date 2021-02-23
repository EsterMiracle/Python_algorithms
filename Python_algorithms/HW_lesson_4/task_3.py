"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Сделайте вывод, какая из трех реализаций эффективнее и почему!!!
И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from random import randint
from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = randint(999999, 9999999999)

print(f'revers_1= {timeit("revers_1(num)", "from __main__ import revers_1, num", number=10000)}')
print(f'revers_2= {timeit("revers_2(num)", "from __main__ import revers_2, num", number=10000)}')
print(f'revers_3= {timeit("revers_3(num)", "from __main__ import revers_3, num", number=10000)}')

cProfile.run("revers_1(num), revers_2(num), revers_3(num)")

# reverse_1 - как мы видим из результатов, здесь рекурсия работает медленее всех, из-за повторных вызовов
# reverse_2 - вариант с циклом работает практически в 2 раза быстрее рекурсии, т.к. нет повторных вызовов
# reverse_3 - вариант со сменной типа из int в строку оказался самым быстрым, т.к. у данной функции вес алгоритма О(n)
