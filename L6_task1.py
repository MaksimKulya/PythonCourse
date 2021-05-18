# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
#
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).

# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:

    def __init__(self, color1, color2, color3):
        self.__color1 = color1
        self.__color2 = color2
        self.__color3 = color3

    # color = ["red", "yellow", "green"]

    def red(self):
        print(self.__color1)
        sec = 0
        while True:
            print(f"{sec + 1} sec")
            time.sleep(1)
            sec += 1
            if sec == 7:
                break

    def yellow(self):
        print(self.__color2)
        sec = 0
        while True:
            print(f"{sec + 1} sec")
            time.sleep(1)
            sec += 1
            if sec == 3:
                break

    def green(self):
        print(self.__color3)
        sec = 0
        while True:
            print(f"{sec + 1} sec")
            time.sleep(1)
            sec += 1
            if sec == 7:
                break

    def running(self):
        print("TrafficLight is on...")
        while True:
            self.red()
            self.yellow()
            self.green()
            self.yellow()


TL1 = TrafficLight("red", "yellow", "green")

TL1.running()
