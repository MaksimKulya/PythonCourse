# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.

# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def summator():
    sum_numb = 0
    while True:
        print(f"Enter the string of numbers with spaces")
        str = (input())
        str=list(str.split()) # убираются пробелы, переводится в список из типа строк
        numb=[] # пустой список для будущих чисел
        for i in range(len(str)):
            if str[i].isdigit(): # если элемент - число, то добавляем в список, предварительно переведя строку в float
                numb.append(float(str[i]))
            else: # если элемент не число, то на данной итерации добавляем в список 0.
                print("No digit element was found. Stop.")
                numb.append(0)
                sum_numb = sum((numb)) + sum_numb # Считаем сумму того что есть
                print(f"Sum = {sum_numb}")
                return 0 # глобальное завершение функции

        # если в else ни разу не попали то считается сумма и переходим в начало цикла
        sum_numb=sum((numb))+sum_numb
        print (f"Sum = {sum_numb}")


summator()

