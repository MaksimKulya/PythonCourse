print("Введите значение выручки")
gain = float(input())

print("Введите значение издержек")
cost = float(input())

if gain > cost:
    print(f"Ваша прибыль = {gain-cost}")
    print(f"Рентабельность Вашей выручки = {100*(gain - cost)/gain:.2f} %")
    print("Введите численность сотрудников Вашей фирмы")
    persons = int(input())
    print(f"Прибыль в расчете на одного сотрудника = {(gain-cost)/persons:.2f}")
else:
    print(f"Ваши убытки = {cost-gain}")
