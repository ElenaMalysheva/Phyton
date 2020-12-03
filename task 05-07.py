# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста


with open("05-07.txt") as f_obj:
    content = f_obj.readlines()
# Подсчитываем среднюю прибыль и составляем  list
i = 0
new_list = []
firm_list = []
sum_list = []
for line in content:
    i +=1
    line = line.split()
    profit = int(line[2]) - int(line[3])
    firm_list.append(line[0])
    new_list.append(profit)
    if profit > 0:
        sum_list.append(profit)

average_sum = sum(sum_list) / i
firm_list.append('average_profit')
new_list.append(average_sum)

"""Составляем словарь"""
my_dict= dict(zip(firm_list, new_list))
print(f'Словарь прибылей наших фирм: , {my_dict}')

"""Переводим в формат Json"""
import json
with open("my_file.json", "w") as write_f:
    json.dump(my_dict, write_f)
print('Словарь в  json-объекте:', json.dumps(my_dict))