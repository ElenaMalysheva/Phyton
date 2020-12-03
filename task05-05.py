# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Читаем-записываем файл
with open("05-05.txt", 'w+') as f_obj:
    f_obj.write("3 5 6 7 8 9 0 6 4 3")
    f_obj.seek(0)
    content = f_obj.readlines()

# Преобразование считанных значений  и расчеты
my_list = content[0]
my_list = my_list.split()
my_list = list(map(int, my_list))
result = sum(my_list)
print(f'Сумма чисел: , {result}')


