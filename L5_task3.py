# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

file = open("text_3.txt", "r", encoding="utf-8")

num_str = len(file.readlines())

file.seek(0)

for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    if float(text2[1]) < 20000:
        print(f"< 20000: {text2[0]}")

file.seek(0)

sum = 0
for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    sum += float(text2[1])

print(f"Average income: {sum / num_str}")

file.close()
