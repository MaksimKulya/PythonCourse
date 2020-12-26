print("Введите результат первого дня")
a = float(input())

print("Введите желаемый общий результат")
b = float(input())

day = 1
while a <= b:
    print(f"День {day}: {a}")
    a = a + 0.1 * a
    day = day + 1
    if a > b:
        print(f"День {day}: {a}")

print(f"Ответ: на {day} день спортсмен достиг результата — не менее {b} км")
