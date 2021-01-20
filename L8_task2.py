# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем.

# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class DivByNull(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    print("Enter divider")
    divider = float(input())

    print("Enter denominator")
    denominator = float(input())

    if denominator == 0:
        raise DivByNull("'Division by zero' error")
except (DivByNull, ValueError) as err:
    print(err)
else:
    print(divider/denominator)
finally:
    print("End")


