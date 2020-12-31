# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Чтение и вывод того, что есть в файле
file = open("text_4.txt", "r", encoding="utf-8")
print(file.read())
print("---------------")

# В виде списка без пробелов
file.seek(0)
num_str = len(file.readlines())
file.seek(0)

for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    print(text2)
print("---------------")

# Замена на русские слова и запись  в новый файл
file.seek(0)

rusnum = ["Один", "Два", "Три", "Четыре"]

file_new = open("text_4new.txt", "w", encoding="utf-8")

for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    text2[0] = rusnum[i]
    print(text2)
    file_new.write(text2[0] + " " + text2[1] + " " + text2[2] + "\n")

file.close()
file_new.close()
