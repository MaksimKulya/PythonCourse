# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Store:

    def __init__(self):
        self.name = ""
        self.price = ""
        self.quantity = ""

        self.unit = {}  # словарь для дальнейшего заполнения объектом
        self.store = []  # список для дальнейшего заполнения словарями


class Equipment(Store):
    def reception(self):

        while True:

            self.name = input(f'Enter name: ')
            self.unit = {}

            while True:
                try:
                    temp = (input(f'Enter price: '))
                    self.price = float(temp)
                except ValueError:
                    print("Value error, try again")
                    continue
                if temp.isdigit():
                    break

            while True:
                try:
                    temp = (input(f'Enter quantity: '))
                    self.quantity = float(temp)
                except ValueError:
                    print("Value error, try again")
                    continue
                if temp.isdigit():
                    break

            text = {'Name': self.name, 'Price': self.price, 'Quantity': self.quantity}
            self.unit.update(text)  # обновляем словарь

            self.store.append(self.unit)  # добавляем словарь в список

            print(f'Current store: \n')
            for key, value in self.store[-1].items():  # красивый вывод словаря
                print("{0}: {1}".format(key, value))

            print(f'q - quit, enter - continue \n')

            if input().lower() == 'q':

                for i in range(len(self.store)):  # красивый вывод итогового словаря
                    for key, value in self.store[i].items():
                        print("{0}: {1}".format(key, value))
                    print("\n")
                break
            else:
                continue


class Printer(Equipment):
    def __init__(self):
        print("Now we collect printers:")
        super().__init__()


class Scanner(Equipment):
    def __init__(self):
        print("Now we collect scanners:")
        super().__init__()


class Xerox(Equipment):
    def __init__(self):
        print("Now we collect xeroxes:")
        super().__init__()


unit_1 = Printer()
print(unit_1.reception())

unit_2 = Scanner()
print(unit_2.reception())

unit_3 = Xerox()
print(unit_3.reception())

