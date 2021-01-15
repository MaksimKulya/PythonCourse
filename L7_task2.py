# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import abstractmethod


class Clothes:
    def __init__(self, cloth):
        self.cloth = cloth

    @abstractmethod
    def calc(self):
        return f'Total cloth consumption: ???'

    @property
    def cloth(self):
        return self.__cloth

    @cloth.setter
    def cloth(self, cloth):
        if cloth < 10:
            self.__cloth = 10
        elif cloth > 500:
            self.__cloth = 500
        else:
            self.__cloth = cloth


class Coat(Clothes):
    def input(self):
        print(f'Input cloth amount for coat: {self.cloth}')

    def calc(self):
        return self.cloth / 6.5 + 0.5

    def calc_show(self):
        print(f'Total cloth consumption for coat: {self.cloth / 6.5 + 0.5 :.2f}')


class Suit(Clothes):
    def input(self):
        print(f'Input cloth amount for suit: {self.cloth}')

    def calc(self):
        return 2 * self.cloth + 0.3

    def calc_show(self):
        print(f'Total cloth consumption for suit: {2 * self.cloth + 0.3 :.2f}')


class Total:
    def __init__(self, summa):
        self.summa = summa

    def show(self):
        print(f"Total sum of all items: {self.summa}")


item1 = Coat(5)  # дает 10, @property работает
item1.input()
item1.calc_show()
print("")

<<<<<<< HEAD
item2 = Coat(550)  # дает 500, @property работает
=======
item2 = Coat(15)  # дает 10, @property работает
>>>>>>> lesson7
item2.input()
item2.calc_show()
print("")

item3 = Suit(600)  # дает 500, @property работает
item3.input()
item3.calc_show()
print("")

# Реализовать общий подсчет расхода ткани удалось только через новый класс Total, где суммируются уже результаты работы метода calc
# Через __add__ не вышло, так как для coat и suit в методе calc для каждого своя формула
sum1 = Total(item1.calc() + item2.calc() + item3.calc())
sum1.show()
