# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


print(f"Enter a1")
a1 = float(input())

print(f"Enter a2")
a2 = float(input())


# by try
def division_try(a1, a2):
    try:
        return a1 / a2
    except ZeroDivisionError:
        return "NaN"


# by if
def division_if(a1, a2):
    if a2 == 0:
        a3 = "NaN"
    else:
        a3 = a1 / a2
    return a3


a3 = division_try(a1, a2)
print(f"a3={a3}")
