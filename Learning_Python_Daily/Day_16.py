# Oops 3rd and 4th Pillar :

# Polymorphism :
'''
Poly = many & Morph = forms
"It means "Same function name or interface , but different behaviour depending on the object"

Ex. 1: Polymorphism with Functions and Classes

class fish:
    def sound(self):
        print("very little sound")

class bacteria:
    def sound(self):
        print("No sound")

def animal_sound(animal):
    print(animal.sound())

f = fish()
b = bacteria()
animal_sound(f)
animal_sound(b)

Ex. 2: Polymorphism with Inheritance (Overriding)

class Employee:
    def work(self):
        print("Works 9 to 5")

class Developer(Employee):
    def work(self):
        print("Works normally")

class Designer(Employee):
    def work(self):  # work() method behaves differently depending on the object
        print("Work good")

# Create a list of objects and iterate over them
for emp in [Developer(), Designer()]:
    emp.work()                              
''' 

# Abstraction :
'''
1. What is Abstraction
    Hiding the internal complex logic and showing only the necessary parts.

Ex.: 
from abc import ABC, abstractmethod

class animal(ABC):

    @abstractmethod
    def speak(self):
        pass
        
#Subclass must override the abstractmethod
class dog(animal):
    def speak(self):
        print("bow boww!!!")

class cat(animal):
    def speak(self):
        print("Meow!!!")

a = dog()
a.speak()
'''