class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Inherits all attributes and methods from Transport

# Create Autobus object
bus = Autobus(name="Renault Logan", max_speed=180, mileage=12)

# Print the result
print(f"Vehicle name: {bus.name} Speed: {bus.max_speed} Mileage: {bus.mileage}")