
from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        # self.vrag = 100

    def run(self, vrag=100):
        day = 0
        print(f"{self.name} на нас напали!!")
        while vrag > 0:
            vrag = vrag - self.power
            time.sleep(day)
            day += 1
            print(f"{self.name} сражается {day} день(дня),  осталось {vrag} воинов!")
            # time.sleep(1)
        print(f"{self.name} одержал победу спустя одержал победу спустя {day} дней(дня)!")
        # print('Все битвы закончились!')




    # def run(self):
    #     print(f"{self.name} на нас напали!!")
    #     for i in range(100):
    #         print(f"{self.name} атакует {i + 1} раз!")
    #         time.sleep(1)
    #     print(f"{self.name} завершил сражение!")

lancelot = Knight('Sir Lancelot', 10)
galahad = Knight('sIR Galahad', 20)
lancelot.start()  # Запускаем поток
galahad.start()
lancelot.join()   # Ждем завершения потока
galahad.join()
print('Все битвы закончились!')