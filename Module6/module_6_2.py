class Vehicle:
    def __init__(self, owner, __model, __engine_power, __colour):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__colour = str(__colour)

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_HP(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_colour(self):
        return f'Цвет: {self.__colour}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_HP()}\n{self.get_colour()}\nВладелец: {self.owner}')

    def set_colour(self, new_colour):
        new_color = str(new_colour.lower())
        if new_color in self.__COLOR_VARIANTS:
            self.__colour = new_colour
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_colour('Pink')
vehicle1.set_colour('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


