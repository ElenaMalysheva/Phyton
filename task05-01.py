# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
#
"""очищаем файл"""
with open("05-01.txt", 'w+') as f_obj:
    f_obj.readline()

with open("05-01.txt", 'a') as f_obj:
    while True:
        data = input('Введите текст:')
        f_obj.writelines(data + '\n')
        if not data:
            break


