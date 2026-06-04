# inheritance 
# polymorphism -> multiple behavior
# abstraction -> only needed info
# encapsulation -> related code togther

# print(3 + 4) #integers 
# print("mahima" + "python") # strings

# print(3 * 3)
# print(3 * "python")

class Vehicle:
    def show(self):
        print("method from vehicle")

class Car(Vehicle):
    def show(self):
        print("car show")

ob1 = Vehicle()
ob2 = Car()

for i in (ob1, ob2):
    i.show()