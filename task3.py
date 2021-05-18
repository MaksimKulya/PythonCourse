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

nn = (n * (10 ** length) + n)
nnn = (nn * (10 ** length) + n)

summa = n + nn + nnn
print(f"Сумма по логике n+nn+nnn = {summa}")
