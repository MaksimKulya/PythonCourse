# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
#
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


obj0 = Stationery("Просто инструмент")
obj0.draw()


obj1 = Pen("Ручка")
obj1.draw()

obj2 = Pencil("Карандаш")
obj2.draw()

obj3 = Handle("Маркер")
obj3.draw()
