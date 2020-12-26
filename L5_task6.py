# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

file = open("text_6.txt", "r", encoding="utf-8")

num_str = len(file.readlines()) # количество строк
file.seek(0)

# находим все числа в каждой строке
aaa=[]
for i in range(num_str):
    text = file.readline()
    text2 = text.split()

    aa=[]
    for j in range(1,len(text2)):
        a = ''.join(k for k in text2[j] if k.isdigit())
        aa.append(a)
    aaa.append(aa)


# заменяем пустые строки на 0 и переводим во float
for i in range(len(aaa)):
    for j in range(len(aaa[i])):
        if aaa[i][j]=="":
            aaa[i][j]="0"
        aaa[i][j]=float(aaa[i][j])


# Снова читается файл, формируется словарь (сделал через цикл и update)
file.seek(0)

slv={}
for i in range(num_str):
    text = file.readline()
    text2 = text.split()
    slv.update({text2[0]:sum(aaa[i])})

print(slv)

