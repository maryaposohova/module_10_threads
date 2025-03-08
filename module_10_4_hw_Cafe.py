# Имитация работы кафе

from threading import Thread
import random
import time
from queue import Queue

class Table:                                                                # Столик, по умолч. свободный
    def __init__(self, number: int):
        self.number = number
        self.guest = None

    # def __str__(self):
    #     if self.guest is None:
    #         return f'Столик № {self.number} свободен'
    #     else:
    #         return f'Столик № {self.number} занят'

# t = Table(1)
# print(t)


class Guest(Thread): # гость поток
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):                                                          # кушают
        time.sleep(random.randint(3,10))


# q = Guest('Вася')
# q.start()


class Cafe:
    def __init__(self, *tables_: Table):
      self.queue = Queue()                                                  # очередь из посетителей
      self.tables = list(tables_)                                           # столы в кафе (список)

    def search_free_table(self):                                            #  ищем свободный столик
        for table in self.tables:
            if table.guest is None:                                         # Если нашли своб. стол, то возвр. стол
                return table
        return None                                                         # если свободных столов нет


    def guest_arrival(self, *guests_: Guest):                               # прибытие гостей
        for guest in guests_:                                               # для данного гостя в списке гостей
            free_table = cafe.search_free_table()
            if free_table:                                                  # если стол свободный
                free_table.guest = guest                                    # то гость занимает его
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:                                                           # если стол занят
                self.queue.put(guest)
                print(f"{guest.name} занимает очередь")

    def discuss_guests(self):  # Обслуживание гостей
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # если стол занят и там поели, гость уходит
                    # Если гость закончил "есть", освобождаем стол
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None                                      # стол освобождается для следующего гостя
                if not self.queue.empty() and table.guest :                 # если еще есть очередь и стол освобожден
                    guest = self.queue.get()                                # берем гостя из очереди
                    guest.start()                                           # обслуживаем
                    print(f"{guest.name} из очереди сел(-а) за стол номер {table.number}")


# c = Cafe()
# print(c.guest_arrival())


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # # Обслуживание гостей
    cafe.discuss_guests()
