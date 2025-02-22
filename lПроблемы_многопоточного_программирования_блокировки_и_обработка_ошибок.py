import threading
'''Проблемы многопоточного программирования, блокировки и обработка ошибок'''

# counter = 0
# lock = threading.Lock()
# print(lock.locked())
#
#
# def increment(nane):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         # print(nane, counter, lock.locked())
#         print(nane, counter)
#     lock.release()
#
#
# def decrement(nane):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter -= 1
#         # print(nane, counter, lock.locked())
#         print(nane, counter)
#     lock.release()


# компактный способ локировки с оператором with
'''Вместо «lock.acquire» и «lock.realise» можно использовать оператор «with»
Укажем имя замка, весь код, который будет идти с отступом после оператора «with», будет выполняться с блокировкой'''
counter = 0
lock = threading.Lock()
print(lock.locked())


# def increment(nane):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter += 1
#             print(nane, counter, lock.locked())
#
#
#
# def decrement(nane):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter -= 1
#             print(nane, counter)

# Конструкция «try» и «finaly» с замками.
def increment(nane):
    global counter
    try:
        lock.acquire()
        for i in range(1000):
            counter += 1
            print(nane, counter, lock.locked())
            # print(nane, counter)
    except Exception:
        pass
    finally:
        lock.release()


def decrement(nane):
    global counter
    try:
        lock.acquire()
        for i in range(1000):
            counter -= 1
            print(nane, counter, lock.locked())
            # print(nane, counter)
    except Exception:
        pass
    finally:
        lock.release()


thread1 = threading.Thread(target=increment, args=('thrread1',))
thread2 = threading.Thread(target=decrement, args=('thrread2',))
thread3 = threading.Thread(target=increment, args=('thrread3',))
thread4 = threading.Thread(target=decrement, args=('thrread4',))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Это может помочь, когда нужно контролировать процесс работы с общими данными.
