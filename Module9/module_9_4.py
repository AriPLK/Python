import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        a = open(file_name, 'w', encoding="utf-8")
        for data in data_set:
            a.write(f'{data}\n')
        a.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        choice = random.choice(self.words)
        return choice

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
