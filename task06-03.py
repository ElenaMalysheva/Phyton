# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name='Борис', surname='Борисович', position='рабочий', par1=0, par2=0):
            self.name =  name
            self.surname = surname
            self.position = position
            self.par1 = par1
            self.par2 = par2
            self._income = {'wage': self.par1, 'bonus': self.par2}

class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(f'Имя и фамилия: {full_name}')

    def get_total_income(self):
        total_income = int(self._income['wage']) + int(self._income['bonus'])
        print(f'Доход: {total_income} руб')

worker = Worker()
position = Position('Василий', 'Васильев', 'главный', 10000, 50000)
position.get_full_name()
position.get_total_income()

position1 = Position('Иван', 'Иванов', 'бухгалтер', 300, 500)
position1.get_full_name()
position1.get_total_income()
