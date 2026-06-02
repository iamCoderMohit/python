# reusabiity
# clean code

# dog -> name, color, breed
# print all info

class Dog:
    #constructor function
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    # #property
    # name = ""
    # color = ""
    # breed = ""

    #method
    def info(self):
        print(f"Name : {self.name}, Color : {self.color}, Breed : {self.breed}")



dog1 = Dog("bruno", "black", "labra")
#bruno, black, labra
# dog1.name = "bruno"
# dog1.color = "black"
# dog1.breed = "labra"
# print(dog1.dogName, dog1.dogColor, dog1.dogBreed)
dog1.info()

dog2 = Dog("kalu", "kala", "desi")
#kaalu, kala, desi
# dog2.name = "kalu"
# dog2.color = "kala"
# dog2.breed = "desi"
# print(dog2.dogName, dog2.dogColor, dog2.dogBreed)
dog2.info()
