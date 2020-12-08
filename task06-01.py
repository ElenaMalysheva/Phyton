# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__colors = {'red': 7, 'yellow': 4, 'green': 7}
    def running(self):
        for el in self.__colors:
            print(el)
            time.sleep(int(self.__colors[el]) * 0.1)

traffic = TrafficLight()
traffic.running()

с = 0
for i in cycle(range(1)):
    traffic.running()
    if с > 10:
        break
    с += 1

