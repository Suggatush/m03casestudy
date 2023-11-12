#Isaac Williams, car.py
#the program asks for and then stores vehicle details as objects and then prints them out
class Vehicle:
  pass
vehicle_type = Vehicle()
  

class Automobile(Vehicle):
  pass
#Creating automobile attributes
year = Automobile()
make = Automobile()
model = Automobile()
doors = Automobile()
roof = Automobile()
#input values
vehicle_type =  input(str("What type of vehicle do you have?"))
year = input(str("What year is your car?"))
make = input(str("What make is your car?"))
model = input(str("What model is your car?"))
doors = input(str("Does your car have 2 or 4 doors?"))
roof = input(str("Does your car have a sunroof or a solid roof"))
#print statements
print("Vehicle type: ",vehicle_type)
print("Year: ", year)
print("Make: " , make)
print("Model: ", model)
print("Doors: ", doors)
print("Roof: ", roof)
