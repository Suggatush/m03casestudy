#Isaac Williams, car.py
#the program asks for and then stores vehicle details as objects and then prints them out
class Vehicle:
  #vehicle_type =  'car'
  #def __init__(self,):
    #self.vehicle = Vehicle.vehicle_type
    #Vehicle.vehicle_type = 'car'

  def vehicle_type(self):
    vehicle_type =  'car'
    print("Vehicle type: ",vehicle_type)
  

class Automobile(Vehicle):
  

  def vehicle_type(self):

    
    year = input(str("What year is your car?"))
    make = input(str("What make is your car?"))
    model = input(str("What model is your car?"))
    doors = input(str("Does your car have 2 or 4 doors?"))
    roof = input(str("Does your car have a sunroof or a solid roof"))

    #print statements
    super().vehicle_type()
    #print("Vehicle type: ",type)
    print("Year: ", year)
    print("Make: " , make)
    print("Model: ", model)
    print("Doors: ", doors)
    print("Roof: ", roof)
#Creating automobile attributes
#year = Automobile()
#make = Automobile()
#model = Automobile()
#doors = Automobile()
#roof = Automobile()

a1 = Automobile()
a1.vehicle_type()