# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list1 = [1, 5.5, "text", [1, 2, 3], True]

print(list1)

for i in range(len(list1)):
    print(f"The type of {i} element is {type(list1[i])}")

