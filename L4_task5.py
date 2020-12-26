# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import random as rnd

a = [rnd.randint(100, 1000) for i in range(10)]
print(f"Initial array: {a}")

from functools import reduce

def my_func(a1, a2):
    return a1 * a2

multi=reduce(my_func, a)
print(f"All elements multiplication = {multi}")