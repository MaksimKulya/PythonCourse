print("Введите целое число 'n' ")
n = int(input())
# -----------------------------
# find length of n
N = n
if N == 0:
    length = 1
else:
    length = 0
    while N != 0:
        N = N // 10
        length = length + 1
# -----------------------------

maximum = n % 10

while length != 0:
    n = n // 10
    maximum_new = n % 10
    if maximum_new <= maximum:
        maximum = maximum
    else:
        maximum = maximum_new
    length = length - 1

print(f"Максимальная цифра в Вашем числе = {maximum}")
