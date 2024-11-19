import threading
import random
import time


lock = threading.Lock()
class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        transactionAmount = 100
        while transactionAmount:
            topUp = random.randint(50, 500)
            self.balance += topUp
            print(f'Пополнение: {topUp}. Баланс: {self.balance}')
            transactionAmount -= 1
            time.sleep(0.001)
            if self.balance >= 500 and lock.locked:
                lock.release()
                break

    def take(self):
        transactionAmount = 100
        while transactionAmount:
            withdraw = random.randint(50, 500)
            print(f'Запрос на {withdraw}')
            if withdraw <= self.balance:
                self.balance -= withdraw
                print(f"Снятие: {withdraw}. Баланс: {self.balance}")
                transactionAmount -= 1
                time.sleep(0.001)
            else:
                print('Запрос отклонён, недостаточно средств')
                lock.acquire()
                break

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')