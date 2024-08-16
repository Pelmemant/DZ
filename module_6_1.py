class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
    edible = False


class Mammal(Animal):
    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print('Животное ' + str(self.name) + ' съел ' + str(food.name))

        else:
            self.alive = False
            print(str(self.name) + ' не стал есть ' + str(food.name))


class Predator(Animal):
    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print('Животное ' + str(self.name) + ' съел ' + str(food.name))

        else:
            self.alive = False
            print(str(self.name) + ' не стал есть ' + str(food.name))


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
