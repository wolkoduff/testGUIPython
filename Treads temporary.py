import time
from threading import Thread, Timer


def sleepMe(cnt):
    print("Вошли в метод в потоке, кстати, это поток № {0}".format(cnt))
    time.sleep(5)
    print("Ожил спустя 5 секунд {0}\n".format(cnt))


def delayed():
    print("Я запущен с таймера")


for i in range(3):
    thread = Thread(target=sleepMe, args=(i,))
    thread.start()
    th = Timer(i + 1, delayed)
    th.start()
