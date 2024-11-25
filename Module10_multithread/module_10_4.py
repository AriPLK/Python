import random
import time
import threading
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def sit_guest(self, guest):
        if self.guest is None:
            self.guest = guest
            return True
        return False

    def leave_guest(self):
        if self.guest is not None:
            self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()
        self.lock = threading.Lock()

    def guest_arrival(self, *guests):
        for guest in guests:
            with self.lock:
                assigned = False
                for table in self.tables:
                    if table.sit_guest(guest):
                        print(f"{guest.name} сел(-а) за стол номер {table.number}")
                        assigned = True
                        guest.start()
                        break
                if not assigned:
                    self.queue.put(guest)
                    print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while any([table.guest is not None for table in self.tables]) or not self.queue.empty():
            for table in self.tables:
                # Проверка, есть ли гость за столом и завершил ли он прием пищи
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла) из стола номер {table.number}")
                    # Освобождение стола
                    table.leave_guest()
                # Если есть свободный стол и очередь не пуста
                if table.guest is None and not self.queue.empty():
                    guest = self.queue.get()
                    print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.sit_guest(guest)
                    guest.start()


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
# Обслуживание гостей
cafe.discuss_guests()