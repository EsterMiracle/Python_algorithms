"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""

import hashlib


def create_login_func():
    hash_file = open("hash_file.txt", "w+")
    if result == result_2:
        print("Ваша связка логин + пароль успешно созданны!")
        return (hash_file.write(str(result)))
    else:
        return "Ваши данные не совпадают!"


salt_login = input("Введите ваше имя логина: ")
password = input("Введите ваш новый пароль: ")
hash_obj = hashlib.sha256(b"password")

result = hashlib.sha256(salt_login.encode() + password.encode()).hexdigest()
print(f"Значение соли: {salt_login}, значение хэша: {password}")
print(f"Результат после кодировки: {result}")

salt_login_2 = input("Повторите ввод вашего логина: ")
password_2 = input("Повторите ввод вашего пароля пароль: ")
hash_obj_2 = hashlib.sha256(b"password")
result_2 = hashlib.sha256(salt_login_2.encode() + password_2.encode()).hexdigest()
print(f"Подтверждённое значение соли: {salt_login_2}, подтверждённое значение хэша: {password_2}")
print(f"Результат после кодировки: {result_2}")

print(create_login_func())
