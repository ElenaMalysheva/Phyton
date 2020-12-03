# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("05-02.txt") as f_obj:
    content = f_obj.readlines()

i = 0
lengh_string = []
for el in content:
    i += 1
    lengh_string.append(len(el.split()))

print("Содержимое файла: ", content)
print("Количество строк в файле: ", i)
print("Количество слов в строке", lengh_string)


