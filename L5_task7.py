# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json


file = open("text_7.txt", "r", encoding="utf-8")

num_str = len(file.readlines()) # количество строк

file.seek(0)
print(file.read())

file.seek(0)

slv1={}

for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    profit=(float(text2[2])-float(text2[3]))
    if profit > 0:
        slv1.update({text2[0]:profit})


print(slv1)

sum=0

for i,j in slv1.items():
    sum+=j

slv2={"Average profit":sum/len(slv1)}
print(slv2)

slv3=[slv1,slv2]
print(slv3)

file2 = open("text_7new.txt", "w", encoding="utf-8")
json.dump(slv3,file2,ensure_ascii=False)