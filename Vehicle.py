# This class represents a single vehicle parent

class Vehicle:
    def __init__(self, park_space):
        self.park_space = park_space

    def get_space(self):
        return self.park_space


# We are taking three vehicles here - Car (size - 1) , Limo (size-2), truck (size-3)

class Car(Vehicle):
    def __init__(self):
        super().__init__(1)


class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)


class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)
