class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read().strip()
        file.close()
        return products

    def add(self, *products):
        prod = self.get_products()
        for product in products:
            product_str = str(product)
            if product_str not in prod:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product_str} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
