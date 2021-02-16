"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""
import random


def guessing_game(count, numb):
    answer = int(input("Введите число от 0 до 100: "))
    if count == 10 or answer == numb:
        if answer == numb:
            print("Вы угадали!!")
        print(f"Загаданное число: {numb}")
    else:
        if answer > numb:
            print(f"Загаданное число меньше чем {answer}!")
        else:
            print(f"Загаданное число больше чем {answer}!")
        guessing_game(count + 1, numb)


guessing_game(1, random.randint(0, 101))