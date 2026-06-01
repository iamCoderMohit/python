# classes and objects
# code reusabilty

# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code

# procedural programming
# oop

# ux -> user experience
# dx -> developer experience

# debug -> fixing errors

# train ->

#form 
# name -> mahima
# age -> 30
# destination -> uk

# blank form is class -> blueprint
# filled form is object

# Almost everything in Python is an object, with its properties and methods.

class RailwayForm:
    # 
    name = "mahima"
    age = 30
    dest = "uk"

obj1 = RailwayForm() # obj1 is object

# print(obj1.name) # mahima
# print(obj1.age)
# print(obj1.dest)

obj2 = RailwayForm() #my form
obj2.name = "mohit"
obj2.age = 45
obj2.dest = "haryana"

# print(obj2.name) #
# print(obj2.age)
# print(obj2.dest)

class Demo():
    # constructor function
    def __init__(self, name, age, dest):
        self.ClassName = name
        self.ClassAge = age
        self.ClassDest = dest

    # normal function / method
    def info(self):
        print(f"Name : {self.ClassName}, Age : {self.ClassAge}, dest : {self.ClassDest}")

p1 = Demo("mahima", 23, "uk")
# p1.info()

p2 = Demo("mohit", 45, "jaipur")
# p2.info()

# class car -> objects with info car's company, car color, car seats

class Car:
    def __init__(self, company, color, seats):
        self.companyName = company
        self.carColor = color
        self.carSeats = seats

    def info(self):
        print(f"Name : {self.companyName}, Color : {self.carColor}, Seats : {self.carSeats}")

# comapnyName = company

car1 = Car("Ferrari", "Red", 2)
car1.info()

car2 = Car("Toyota", "Black", 8)
car2.info()