# Base Class
class Vehicle:
    def move(self):
        return "This vehicle moves."

# Inherited Class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Inherited Class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Inherited Class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Example Usage
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
