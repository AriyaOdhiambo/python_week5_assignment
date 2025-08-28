# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived classes with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Testing polymorphism
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bicycle()]

    for v in vehicles:
        v.move()  # Each one responds differently
