# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

with open("05-04.txt") as f_obj:
    content = f_obj.readlines()

print(content)
new_list = []

for el in content:
    a = (el.split())
    if a[0] == 'One':
        a[0] = 'Один'
    elif a[0] == 'Two':
        a[0] = 'Два'
    elif a[0] == 'Three':
        a[0] = 'Три'
    elif a[0] == 'Four':
        a[0] = 'Четыре'
    a.append("\n")
    new_list.append(' '.join(a))

print(new_list)

with open("05-04-01.txt", 'w') as f_obj:
    f_obj.writelines(new_list)
