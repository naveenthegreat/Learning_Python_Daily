#Object-Oriented Programming (OOP) :

'''
✅ What is OOP?
OOP is a programming style where we organize code using:

    Classes → blueprints for objects
    Objects → real things created from classes
    Attributes → data stored in objects
    Methods → actions an object can perform


1. Define a Class

class student:
    pass
    
2. Create an object(Instance):

s1=student()
print(s1)

3. Add Attributes with __init__():

class student:
    def __init__(self,name,age):              # __init__() = constructor (runs when object is created)
        self.name = name                      # self = refers to the current object
        self.age = age          

    s1 = Student("Naveen", 21)
    print(s1.name)  # Naveen

4. self Keyword
"self" refers to the current object (like this in Java/C++).

'''

class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f"The Car brand is {self.brand} and model is {self.model}")

car2=car("Tata","Minitata")
car2.display()


