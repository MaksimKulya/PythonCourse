# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


print(f"Enter the string with spaces")
str = (input())

words=list(str.split())

for i in range(len(words)):
    print(f"{i+1} word: {words[i][0:10]}")