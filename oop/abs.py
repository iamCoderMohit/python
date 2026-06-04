from abc import ABC, abstractmethod

#decorator

# greet()

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass # abstract class

    @abstractmethod
    def sum(self):
        pass

class NewClass(Greet):
    def say_hello(self):
        return print("say hello")
    
ob1 = NewClass()
ob1.say_hello()