import threading
import time
import inspect
from pprint import pprint

class Knight(threading.Thread):
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

def introspection_info(obj):
    _type = type(obj)
    _attributes = inspect.getfullargspec(obj)
    _methods = [x for x in dir(obj) if x.endswith('__')]
    _module = inspect.getmodule(obj)
    _dictInfo = {'type': _type, 'attributes': _attributes, 'methods': _methods, 'module': _module}
    return _dictInfo


number_info = introspection_info(Knight)
pprint(number_info)