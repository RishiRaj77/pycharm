# Example of a simple class in Python

# Define a class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    # Method to start the car
    def start(self):
        self.is_running = True
        print(f"The {self.year} {self.brand} {self.model} starts.")

    # Method to stop the car
    def stop(self):
        self.is_running = False
        print(f"The {self.year} {self.brand} {self.model} stops.")


# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)

# Using the objects
car1.start()
car2.start()

car1.stop()
