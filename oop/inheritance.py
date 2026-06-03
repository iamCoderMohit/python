# 4 pillars of oop

# inheritance 
# polymorphism -> multiple behavior
# abstraction -> only needed info
# encapsulation -> related code togther

class Vehicle: # parent class / base class
    def __init__(self, wheels, color):
        self.wheels = wheels
        self.color = color

    def info(self):
        print(f"Wheels: {self.wheels}, Color: {self.color}")

class Bike(Vehicle): # child class / derived class
    def __init__(self, wheels, color, company):
        super().__init__(wheels, color)
        self.company = company

    # def info(self):
    #     super().info()
    #     print(f"Company: {self.company}")

veh1 = Vehicle("4", "Red")
# veh1.info()

bike1 = Bike(2, "Black", "RE")
# bike1.info()


# multiple inheritance -> more than one parent

class Mother:
    mothername = ""

    def func1(self):
        print("hi from mother")

class Father:
    fathername = ""

    def func2(self):
        print("hi from father")

class Son(Mother, Father):
    def info(self):
        print(f"Mother Name: {self.mothername}, Father Name: {self.fathername}")

s1 = Son()

s1.mothername = "Tracey"
s1.fathername = "John"

# s1.info()

# https://www.geeksforgeeks.org/python/types-of-inheritance-python/