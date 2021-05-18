# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

list = [7, 5, 4, 2, 1]

while True:
    print(f"Enter the number")
    N = int(input())

    if N<min(list):
        list.append(N)
    elif N>max(list):
        list.insert(0,N)
    else:
        for i in range(len(list)):
            if list[i] >= N >= list[i + 1]:
                list.insert(i + 1, N)
                break

    print(list)



