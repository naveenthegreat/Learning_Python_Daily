# Encapsulation 
'''
1. What is Encapsulation?
    Encapsulation means hiding the internal details of how a class works, and only exposing 
    what is necessary.

2. Access Modifiers :

Modifier            Syntax              Access

Public             self.name            Anywhere
Protected         _self._name           Suggest internal use(can still access)
Private           self.__name           Name mangling -> not directly accessible

Mangling -> a process in python uses to make private variables less accessible by automatically
            changing their name internally.

Ex.:

class demo:
    def __init__(self):
        self.name = "Public"
        self._age = 21
        self.__salary = 5000000

d = demo()
print(d.name)              # ✅ Accessible  
print(d._age)              # ✅ Accessible but not recommended
print(d.__salary)          # ❌ Error


3. Why Use Encapsulation ?

Reason                                              Benefits

Hide internal state                         Prevent misuse
Control access to variables                 Add validation, checks
Maintain clean design                       Reusable, safe, predictable
Prevent accidental changes                  Like overwriting balance directly


4. Property Decprators (@property)

Want to access private variables like attributes, but still protected?
Use @property

Ex.:

class product:
    def __init__(self,price):
        self.__price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        if value > 0:
            self.__price = value

        else :
            print("Invalid Price")

p = product(500)
print(p.price)              #Access like a variable, not method
p.price = -100              #Rejected
p.price = 600               #Updated
print(p.price)
'''
