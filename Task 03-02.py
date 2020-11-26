# Реализовать функцию, принимающую несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, god, gorod, em, telefon):
    print(name, surname, god, gorod, em,telefon)

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
god = input("Введите год рождения: ")
gorod = input("Введите город проживания: ")
em = input("Введите email: ")
telefon = input("Введите телефон: ")

my_func(name, surname, god, gorod, em, telefon)

