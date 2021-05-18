# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

file = open("text_3.txt", "r", encoding="utf-8")

num_str = len(file.readlines())
print(f"Number of strings in file: {num_str}")

file.seek(0)

for i in range(num_str):
    text = file.readline()
    num_words = text.count(" ") + 1
    print(f"In {i + 1} line there are {num_words} words")

file.close()
