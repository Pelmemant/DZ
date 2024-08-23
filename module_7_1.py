from pprint import pprint


class Product:
    def __init__(self, name, weight, category, ):
        self.name = name
        self.weight = weight
        self.category = category
        self.a = f'{self.name}, {self.weight}, {self.category}'

    def __str__(self):
        return self.a


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        existing_products = set()
        file_name = self.__file_name

        file = open(file_name, 'r')
        for line in file:
            existing_products.add(line.split(',')[0])
        file.close()

        file = open(file_name, 'a')
        for product in products:
            if product.name not in existing_products:
                file.write(str(product) + '\n')
            else:
                print(f"Продукт {product} уже есть в магазине")
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
