class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def movement(self):
        pass

class Mammal(Animal):
    def sound(self):
        return "Mammal sound"

    def movement(self):
        return "Mammal movement"

class Bird(Animal):
    def sound(self):
        return "Bird sound"

    def movement(self):
        return "Bird movement"

class Fish(Animal):
    def sound(self):
        return "Fish sound"

    def movement(self):
        return "Fish movement"

def simulate_animals(animals):
    for animal in animals:
        print("Name:", animal.name)
        print("Sound:", animal.sound())
        print("Movement:", animal.movement())
        print()

lion = Mammal("Lion")
eagle = Bird("Eagle")
shark = Fish("Shark")

simulate_animals([lion, eagle, shark])
