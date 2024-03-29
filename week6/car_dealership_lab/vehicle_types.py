"""
define classes Car, Truck and Motorcycle in this file 
They should extend the Vehicle base class 
"""
from vehicle import Vehicle

class Car(Vehicle):
  wheels = 4
  type = "car"
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super().__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s

class Motorcycle(Vehicle):
  wheels = 2
  type = "bike"
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super().__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s

class Truck(Vehicle):
  wheels = 18
  type = "truck"
  def __init__(self, miles, make, model, year,fuelC):
    vin=input("what is the VIN number?")
    self.vin=vin
    self.fuelC=fuelC
    super().__init__(miles, make, model, year)

  def __str__(self):
    s= super().vehicle_type()
    s =s + "\n Year: " + str(self.year)
    s= s + "\n Miles: " + str(self.miles)
    return s

