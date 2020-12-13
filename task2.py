print("Введите количество секунд")
sec = int(input())

min = sec // 60
new_sec = sec - min * 60

hour = min // 60
new_min = min - hour * 60

print(f"Данное количество секунд соответствует {hour}ч:{new_min}м:{new_sec}с")
