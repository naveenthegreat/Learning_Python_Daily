# Inheritance (Oops 1st Pillar)
'''
1. What is Inheritence?
    Inheritence means a class(child) can use code of another class(parents).

Ex.: 
class animal:
    def sound(self):
        print("Animals sounds different and some animals crazy")

class dog(animal):
    def bark(self):
        print("Dog bark as bow!! bow!!!")

d=dog()
d.sound()                       # from parent class
d.bark()                        # from child class


2. Types Of Inheritence:

Type                        Descriptions                            Examples

Single                  1 parent, 1 child                       class B(A)
Multiple               multiple parents                         class C(A, B)
Multilevel              Grandparent-> Parent-> Child            class C(B)
Hierarchical            1 parent, many child                    class B(A), class C(A)  

3. super() Method :
    super() is used inside a child class to call methods or constructors from the parent
    class.
    Mainly used when you override the __inti__ methods or other methods.

Ex.:

class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # Calls Animal's constructor
        print("Dog Created")

4. Method Overriding :
    If a child class has a method with the same names as in the parent, it 
    overrides it.

Ex.:

class animal:
    def sound(self):
        print("Sound is generic")

class cat(animal):
    def sound(self):
        print("Meow Meow")

c=cat()
c.sound()
''' 
