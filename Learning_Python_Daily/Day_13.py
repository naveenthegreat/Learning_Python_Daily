# 1. Instance variables vs Class variables
'''
Type                    Definition                  Belongs to                  Example

Instance        Inside __init__ using self        Specific object            self.name = "Naveen"
Class             Directly inside class         Shared by all objects        language = "Python"
                   (outside methods)
'''

# 2. Methods In class :
'''
Type                  Used for                            Syntax

Instance           Access object data                  def method(self)
Class              Access class data                @classmethod def method(cls)
Static           Utility,doesn't access             @staticmethod def method()
                    object or class   
'''

# 3. Multiple Objects in OOP :
'''
Python allows you to create multiple objects using the same class.

p1 = student("Alice")
p2 = student("Ash")
p3 = student("John")
'''