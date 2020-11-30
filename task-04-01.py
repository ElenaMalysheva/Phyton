# coding= UTF-8
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# from sys import argv
#
# script_name, first_param, second_param, third_param = argv
#
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)

from sys import argv
my_link = argv[0]
print(my_link)

if argv == [my_link]:
    print("Введите следующие параметры: выработка в часах, ставка в час, премия: ")
else:
    script_name, first_param, second_param, third_param = argv[0:]
    print("Name script: ", script_name)
    print("Working hours: ", first_param)
    print("Rate in hours: ", second_param)
    print("Prize: ", third_param)
    print("Salary: ", int(first_param) * int(second_param) + int(third_param))
