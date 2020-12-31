# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open("task5.txt", "w+")
file.write(input())

file.seek(0)

text = file.readline()
text2 = text.split()

try:
    text3 = list(map(float, text2))
    print(f"Sum: {sum(text3)}")
except ValueError:
    print("Not a number exists!")

file.close()
