class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Create Autobus object
bus = Autobus("Renault Logan", 180, 12)

# Call the method with default capacity
print(bus.seating_capacity())