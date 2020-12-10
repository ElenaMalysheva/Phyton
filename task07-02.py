# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    @abstractmethod
    def my_clothes_1(self):
        pass

    @abstractmethod
    def my_clothes_2(self):
        pass


class MyClothes(MyAbsClass):
    def __init__(self, v, h):
        self.v = v
        self.h = h


    def my_clothes_1(self):
        rashod_1 = self.v / 6.5 + 0.5
        return rashod_1

    def my_clothes_2(self):
        rashod_2 = self.h * 2 / 100 + 0.3
        return rashod_2

    @property
    def print_all(self):
        return (self.my_clothes_1() + self.my_clothes_2())




my_cloves = MyClothes(56, 180)
print("Расход ткани на пальто:"'{:.2f}' .format(my_cloves.my_clothes_1()))
print("Расход ткани на костюм:"'{:.2f}' .format(my_cloves.my_clothes_2()))

print("Общий расход ткани в метрах:  ", '{:.2f}' .format(my_cloves.print_all))

