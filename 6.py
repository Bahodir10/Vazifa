import random

class Vehicle:
    def __init__(self, speed, passenger_capacity):
        self.speed = speed
        self.passenger_capacity = passenger_capacity

    def accelerate(self):
        self.speed += 10

    def brake(self):
        if self.speed >= 10:
            self.speed -= 10

    def react_to_traffic(self):
        if random.random() < 0.5:
            self.accelerate()
        else:
            self.brake()

class Car(Vehicle):
    def __init__(self, speed, passenger_capacity):
        super().__init__(speed, passenger_capacity)

    def react_to_traffic(self):
        if random.random() < 0.7:
            self.accelerate()
        else:
            self.brake()

class Bicycle(Vehicle):
    def __init__(self, speed, passenger_capacity):
        super().__init__(speed, passenger_capacity)

    def react_to_traffic(self):
        if random.random() < 0.3:
            self.accelerate()
        else:
            self.brake()

class Truck(Vehicle):
    def __init__(self, speed, passenger_capacity, cargo_capacity):
        super().__init__(speed, passenger_capacity)
        self.cargo_capacity = cargo_capacity

    def react_to_traffic(self):
        if random.random() < 0.4:
            self.accelerate()
        else:
            self.brake()

vehicles = [Car(60, 4), Bicycle(20, 1), Truck(50, 2, 5000)]

for _ in range(5):
    for vehicle in vehicles:
        vehicle.react_to_traffic()
        print(f"Vehicle: {type(vehicle).__name__}, Speed: {vehicle.speed}")

    print()
