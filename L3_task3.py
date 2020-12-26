# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def sum_of_two(a1, a2, a3):
    return sum([a1, a2, a3]) - min([a1, a2, a3])


print(f"Enter a1")
a1 = float(input())

print(f"Enter a2")
a2 = float(input())

print(f"Enter a3")
a3 = float(input())

print(sum_of_two(a1, a2, a3))
