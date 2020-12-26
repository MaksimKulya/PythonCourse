# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


print(f"Enter the word")

words = (input())

words_list = words.split()
print("Initial words: ")
print(words_list)

words_list_new = []

for i in range(len(words_list)):
    do_append = 1
    for j in range(len(words_list[i])):
        if (ord(words_list[i][j]) < 97 or ord(words_list[i][j]) > 122) and (
                ord(words_list[i][j]) < 65 or ord(words_list[i][j]) > 90):
            do_append = 0
            break

    if do_append == 1:
        words_list_new.append(words_list[i])

print("Only latin words: ")
print(words_list_new)


def titla(word_list):
    word_list_title = []
    for i in range(len(word_list)):
        word_list_title.append(word_list[i].title())
    print(word_list_title)


print("Titled latin words: ")
titla(words_list_new)
