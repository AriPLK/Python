import threading
from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power, delay, enemies=100):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.delay = delay
        self.enemies = enemies

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.enemies:
            self.enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days} день(дня)... осталось {self.enemies} воинов")
            time.sleep(self.delay)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')
        return days


first_knight = Knight('Sir Lancelot', 10, 1)
second_knight = Knight("Sir Galahad", 20, 1)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
if not first_knight.is_alive() and not second_knight.is_alive():
    print("Все битвы закончились!")
