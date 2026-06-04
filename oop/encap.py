class Parent:
    def __init__(self, pname, lname):
        self.__pname = pname # private property
        self._lname = lname # protected property

    def show(self):
        self.__pname = "random"
        print(self.__pname)

class Child(Parent):
    def __init__(self, pname):
        super().__init__(pname)

    def show(self):
        print(self.__pname)

o1 = Parent("mohit", "joshi")
print(o1._Parent__pname) # name mangling
# o1.show()
# print(o1._lname)

# o2 = Child("mahima")
# print(o2.__pname)
# o2.show()

#https://www.w3schools.com/python/python_encapsulation.asp