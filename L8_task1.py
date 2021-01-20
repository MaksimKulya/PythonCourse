# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число».
#
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_dmy(cls, calendar):
        dmy = calendar.split("-")

        day = int(dmy[0])
        month = int(dmy[1])
        year = int(dmy[2])

        return cls(day, month, year)

    @staticmethod
    def valid(obj):

        if 1 <= obj.day <= 31:
            if 1 <= obj.month <= 12:
                if 0 <= obj.year <= 9999:
                    print('Correct')
                else:
                    print('Wrong year')
            else:
                print('Wrong month')
        else:
            print('Wrong day')


data1 = Data.set_dmy('11-13-2001')
print(data1.day)
print(data1.month)
print(data1.year)
Data.valid(data1)
