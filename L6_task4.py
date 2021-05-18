# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
#
# Для классов TownCar и WorkCar переопределите метод show_speed.
#
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print("Go")

    def stop(self):
        print("Stop")

    def turn(self, direction):
        print(f"Turn {direction}")

    def show_speed(self):
        print(f"Speed is: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        print(f"Speed is: {self.speed}") if self.speed < 60 else print("The speed is over limit 60")


class SportCar(Car):
    def show_speed(self):
        print(f"Speed is: {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        print(f"Speed is: {self.speed}") if self.speed < 40 else print("The speed is over limit 40")


class PoliceCar(Car):
    def show_speed(self):
        print(f"Speed is: {self.speed}")


car1=TownCar(70,"beige","volvo",False)
print(car1.name)
car1.go()
car1.turn("right")
car1.show_speed()

print("")

car2=SportCar(70,"yellow","ferrari",False)
print(car2.name)
car2.go()
car2.turn("left")
car2.show_speed()

print("")

car3=WorkCar(80,"blue","ford",False)
print(car3.name)
car3.go()
car3.turn("left")
car3.show_speed()

print("")

car4=PoliceCar(50,"black","kamaz",True)
print(car4.name)
car4.go()
car4.stop()
car4.show_speed()