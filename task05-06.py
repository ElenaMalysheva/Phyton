# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("05-06.txt", 'r') as f_obj:
    content = f_obj.readlines()
print(f'Исходный файл: , {content}')

sibject = []
lesson = []
for data in content:
    data = data.split()
    new_data = []
    for el in data:
        if el.endswith(':'):
            el = el.strip(':')
            sibject.append(el)
        elif el == '—':
            el = 0
            new_data.append(el)
        elif el.endswith('(л)'):
            el = el.strip('(л)')
            new_data.append(el)
        elif el.endswith('(пр)'):
            el = el.strip('(пр)')
            new_data.append(el)
        elif el.endswith('(лаб)'):
            el = el.strip('(лаб)')
            new_data.append(el)
        else:
            new_data.append(el)
        new_data = list(map(int, new_data))
    hours = sum(new_data)
    lesson.append(hours)


my_dict= dict(zip(sibject, lesson))
print(f'Словарь: , {my_dict}')







