class Cat():
    def __init__(self, animal, food, drink):
        self.animal = animal
        self.food = food
        self.drink = drink

    def eat_like(self):
        print(f'{self.animal}爱吃{self.food},{self.animal}要喝{self.drink}')


one = Cat('小猫', '鱼', '水')
one.eat_like()
