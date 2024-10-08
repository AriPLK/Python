class House:
    def __init__(self, name, number_0f_floors):
        self.name = name
        self.number_of_floors = number_0f_floors

    def go_to(self, new_floor):
        for a in range(new_floor):
            if new_floor > self.number_of_floors:
                print('Такого этажа не существует')
                break
            print(a + 1)
            a += 1
            


h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)