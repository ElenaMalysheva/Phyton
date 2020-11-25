# # task 1
#
# list = [2, 'text', 435, 345.345, 876]
# print(list)
#
# # print(type(list[3]))
# # print(len(list))
# # проверка на тип данных
# l = len(list) - 1
# i = 0
# while i <= l:
#     print(type(list[i]))
#     i += 1
# #     _________________________
# # task 2
#
# list = input("Введите элементы списка: ")
# # Вычисляем четное количество элементов
# l = (len(list) // 2)* 2
# # Создаем новый список
# new_list = []
# i = 0
# while i < (l-1):
#     # Заполняем новый список в нужном порядке
#     new_list.append(list[i + 1])
#     new_list.append(list[i])
#     i += 2
#
# # Добавляем нечётный элемент, если он есть
# if (len(list)) > l:
#     new_list.append(list[l])
# else: list = new_list.copy()
# list = new_list.copy()
# print('Ваш список с новым порядком элементов: ', list)


# ----------------------------
# # task 3
#
# n = int(input('Введите номер месяца в виде целого числа: '))
#
# list = (0, 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима')
# print('Время года: ', list[n])
#
# my_dict = {1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна", 6:"лето", 7:"лето", 8:"лето", 9:"осень", 10:"осень", 11:"осень", 12:"зима"}
# print('Время года: ', my_dict.setdefault(n))

# ----------------------------
# task 4
#
# string = input("Введите несколько слов, разделенных пробелами: ")
# list = string.split()
#
# # i - порядковый номер
# i = 1
# for el in list:
#     if len(el) > 10:
#         print(i, '.', el[0:10])
#     else: print(i, '.', el)
#     i +=1


# --------------------------
# task 5
#
# my_list = [7, 5, 3, 3, 2]
# n = int(input("Введите натуральное число: "))
# for el in my_list:
#     # проверяем первую цифру списка
#     if my_list[0] < n:
#         my_list.insert(0, n)
#         break
#     #     проверяем остальные цифры
#     elif n >= (el + 1):
#         num = my_list.index(el)
#         my_list.insert(num, n)
#         break
# #         вывод последней цифры списка
# else:
#     my_list.append(n)
#
# print("Новый набор натуральных чисел: ", my_list)


