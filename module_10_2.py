from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(self.name + ' на нас напали!')
        enemy = 100
        days = 0
        while enemy > 0:
            print(self.name + "Сражаеться с врагами, "+ str(days) + " дней. Осталось врагов " + str(enemy) + '!')
            enemy -= self.power
            days += 1
            sleep(1)
            if enemy <= 0:
                print(self.name + 'Победил всех врагов за ' + str(days) + ' дней')


first_knight = Knight('Сэр Ланцелот', 10)
second_knight = Knight("Сэр Галахед", 20)

first_knight.start()
second_knight.start()