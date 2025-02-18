# # Потоки на классах
import threading
import time
from time import ctime


class MyThreading(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')


thread1 = MyThreading('thread1', 5, 1)
thread2 = MyThreading('thread2', 3, 2)
thread1.start()
thread2.start()

# import threading
# import time
#
# # Создаем класс, наследующийся от threading.Thread
# class MyThread(threading.Thread):
#     def __init__(self, thread_id, name, delay):
#         threading.Thread.__init__(self)  # Инициализируем базовый класс
#         self.thread_id = thread_id
#         self.name = name
#         self.delay = delay
#
#     # Метод run() будет выполняться в отдельном потоке
#     def run(self):
#         print(f"Поток {self.name} запущен")
#         self.print_numbers()
#         print(f"Поток {self.name} завершен")
#
#     # Вспомогательный метод для выполнения задачи
#     def print_numbers(self):
#         for i in range(5):
#             time.sleep(self.delay)
#             print(f"{self.name}: {i}")
#
# # Создаем экземпляры потоков
# thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 1.5)
#
# # Запускаем потоки
# thread1.start()
# thread2.start()
#
# # Ждем завершения потоков
# thread1.join()
# thread2.join()
#
# print("Все потоки завершены")


