
"""Банковское дело"""

# from threading import Thread, Lock
# import time
# from random import randint
#
#
# class Bank:
#     def __init__(self):
#         self. lock = Lock()
#         self.balance = 0
#
#     def deposit(self):
#         for _ in range(100):
#             random_sum = randint(50, 500)
#             with self.lock:  # Используем блокировку для защиты критической секции
#                 self.balance += random_sum
#                 print(f"Пополнение: {random_sum}. Баланс: {self.balance}")
#                 if self.balance >= 500 and self.lock.locked():
#                     # Это условие не имеет смысла, так как блокировка автоматически снимается после выхода из with
#                     pass
#             time.sleep(0.001)  # Сон вне критической секции
#
#     def take(self):
#         for _ in range(100):
#             random_sum = randint(50, 500)
#             with self.lock:  # Используем блокировку для защиты критической секции
#                 print(f"Запрос на {random_sum}")
#                 if random_sum <= self.balance:
#                     self.balance -= random_sum
#                     print(f"Снятие: {random_sum}. Баланс: {self.balance}")
#                 else:
#                     print(f"Запрос отклонён, недостаточно средств")
#             time.sleep(0.003)  # Задержка вне критической секции
#
#
# bk = Bank()
#
# # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
# th1 = Thread(target=Bank.deposit, args=(bk,))
# th2 = Thread(target=Bank.take, args=(bk,))
#
# th1.start()
# th2.start()
# th1.join()
# th2.join()

# print(f'Итоговый баланс: {bk.balance}')

"""С синхронизацией потоков"""
# Синхронизация потоков, чтобы потоки ждали и уведомляли друг друга о завершении орерации.

from threading import Thread, Lock, Condition
import time
from random import randint


class Bank:
    def __init__(self):
        self. lock = Lock()
        self.balance = 0
        self.condition = Condition(self.lock) # условие для синхронизации
        self.is_deposit_turn = True # флаг очереди

    def deposit(self):
        for _ in range(100):
            random_sum = randint(50, 500)
            with self.condition:  # Используем Condition для синхронизации
                # Ждем, пока не наступит очередь пополнения
                while not self.is_deposit_turn:
                    self.condition.wait()

                # Критическая секция: пополнение баланса
                self.balance += random_sum
                print(f"Пополнение: {random_sum}. Баланс: {self.balance}")

                # Передаем очередь снятию
                self.is_deposit_turn = False
                self.condition.notify()  # Уведомляем поток снятия

            time.sleep(0.001)  # Задержка вне критической секции

    def take(self):
        for _ in range(100):
            random_sum = randint(50, 500)
            with self.condition:  # Используем Condition для синхронизации
                # Ждем, пока не наступит очередь снятия
                while self.is_deposit_turn:
                    self.condition.wait()

                # Критическая секция: снятие средств
                print(f"Запрос на {random_sum}")
                if random_sum <= self.balance:
                    self.balance -= random_sum
                    print(f"Снятие: {random_sum}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")

                # Передаем очередь пополнению
                self.is_deposit_turn = True
                self.condition.notify()  # Уведомляем поток пополнения

            time.sleep(0.003)  # Задержка вне критической секции


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')

