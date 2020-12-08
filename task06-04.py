# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed='speed', color='color', name='name', is_police='false'):
            self.speed =  speed
            self.color = color
            self.name = name
            self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} {self.color} остановилась')
    def turn(self):
        print("Машина повернула")
    def show_speed(self, speed=0):
        print("Скорость машины: ", self.speed)

class TownCar(Car):
    def show_speed(self, speed=0):
        if speed > 60:
            print("Вы превысили скорость! ", speed)
        else:
            print("Скорость машины: ", speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self, speed=0):
        if speed > 40:
            print("Вы превысили скорость! ", speed)
        else:
            print("Скорость машины: ", speed)

class PoliceCar(Car):
    pass

car = Car(60, 'красная', 'BMW', 'false')
car.go()
car.stop()
car.turn()
car.show_speed(60)

towncar = TownCar(80, 'черная' , 'ЛадаКалина', 'false')
towncar.go()
towncar.show_speed(90)

workcar = WorkCar(25, 'желтая' , 'Трактор', 'false')
workcar.go()
workcar.stop()
workcar.show_speed(55)