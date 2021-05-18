# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


print(f"Enter the desirable number of elements of your list")
N = int(input())

print(f"Enter step-by-step {N} elements of your list")
list=[]
for i in range(N):
    list.append(input())

print(list)

j = 0
for i in range(len(list) // 2):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2

print(f"The changed list is {list}")

