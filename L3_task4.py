# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

while True:
    print(f"Enter real positive x")
    x = float(input())
    if isinstance(x, float) and x > 0:
        break
    else:
        print("Try again !")

while True:
    print(f"Enter integer negative y")
    y = int(input())
    if isinstance(y, int) and y < 0:
        break
    else:
        print("Try again !")


def power1(x, y):
    return (1 / x) ** (-y)


def power2(x, y):
    z = 1
    for i in range(-y):
        z = z * (1 / x)
    return z


print(power1(x, y))

print(power2(x, y))

# Какая та странная потеря точности:
# например для 10**-2 будет точное значение 0.01, а (1/10)**2 = 0.010000000000000002