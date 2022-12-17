""" class Elevator:
    def __init__(self, starting_floor):
        self.make = 'The elevator company'
        self.floor = starting_floor
        
# To create the object

elevator = Elevator(1)
print(elevator.make)
print(elevator.floor) """

# The wrong form of "self"
class Car:
    def __init__(self, Hybrid):
        self.tipo = "Hybrid"
        self.color = "Red" # ends up on the object
        self.make = "Mercedes" # becomes a local variable in the constructor

car = Car(2)
print(car.tipo) #Hybrid
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object