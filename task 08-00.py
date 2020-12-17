
"""Добрый день! Карточку создала, игра в принципе близка к решению, но не хватило времени на доработку и оформления.
Что не успела:
-добавить карточку компьютера
-вычеркивать отыгравшие номера (игра пишет про поиск и вычеркивание)
"""

import random

class Loto:

    def __init__(self):
        self.list_first = []
        self.list_second = []
        self.list_third = []
        self.order_of_none = []
        self.list_15 = []
        self.play_bool = bool(1)
        self.bool_for_print = True

    def generate_card(self):
        list_1 = [el for el in range(1, 91)]
        random.shuffle(list_1)
        list_of_15 = []

        i = 0
        for el in list_1:
            if i < 15:
                list_of_15.append(list_1[i])
                i += 1
        self.list_15 = list_of_15

        j = 0
        for el in list_of_15:
            if j < 5:
                self.list_first.append(list_of_15[j])
                j += 1
            elif j < 10:
                self.list_second.append(list_of_15[j])
                j += 1
            elif j < 16:
                self.list_third.append(list_of_15[j])
                j += 1
        return self.list_first.sort(), self.list_second.sort(), self.list_third.sort()

    @staticmethod
    def order_of_pustota(self):
        list_pustota = [el for el in range(0, 10)]
        random.shuffle(list_pustota)
        my_list = []
        i = 0
        for el in list_pustota:
            if i < 4:
                my_list.append(list_pustota[i])
                i += 1
        my_list.sort()
        self.order_of_none = my_list
        return self.order_of_none

    @staticmethod
    def print_card(self):
        """Добавляем пустоты в наш список"""
        if self.bool_for_print == True:
            Loto.order_of_pustota(self)
            for el in self.order_of_none:
                self.list_first.insert(el, ' ')

            Loto.order_of_pustota(self)
            for el in self.order_of_none:
                self.list_second.insert(el, ' ')

            Loto.order_of_pustota(self)
            for el in self.order_of_none:
                self.list_third.insert(el, ' ')

        print("-----Ваша карточка-----")
        print(' '.join([str(i) for i in self.list_first]))
        print(' '.join([str(i) for i in self.list_second]))
        print(' '.join([str(i) for i in self.list_third]))
        print("----------------------")
        return self.list_first.insert, self.list_second, self.list_third

    @staticmethod
    def step_of_game(self):
        list_1 = [el for el in range(1, 91)]
        random.shuffle(list_1)
        keg = list_1[0]
        print("Номер бочёнка: ", keg)

        my_select = input("Выбирете y/n: ")
        if my_select == 'y':
            for el in self.list_15:
                if el == keg:
                    self.play_bool = True
                    print('!!!ищем цифру и зачеркиваем!!!')
                    break

                else: 
                    print('Game over')
                    self.play_bool = False
                    break
        elif my_select == 'n':
            for el in self.list_15:
                if el == keg:
                    print('Game over')
                    self.play_bool = False
                    break
                else:
                    self.play_bool = True
        return self.play_bool


    def play(self):

        while self.play_bool == True:
            Loto.print_card(self)
            Loto.step_of_game(self)
            self.bool_for_print = False




klient = Loto()
klient.generate_card()
klient.play()



