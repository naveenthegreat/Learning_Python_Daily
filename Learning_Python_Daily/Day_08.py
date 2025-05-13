#Function
'''
Function is a reusable block of code that performs specific type.
There are two types of funtion:
            1. Built-in: len(),print(),input(),type()
            2. User-defined: def

#Syntax of function

                def function_name(parameters):
                    # code block
                    return result

def greet():
    print("Hello Naveen")

1. def= defines a function
2. greet= name of function
3. ()= it can hold parameters
4. print()= the logic inside the function
5. greet()= calls the function

#Parameters Vs Arguments

def add(a, b):
    return a + b

print(add(3, 4))  # 7

Parameters: variable names in function definition(a,b)
Arguments: actual values passsed during call(3,4)

#Variable-Length Arguments

➤ *args = many positional arguments
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))  # 10

➤ **kwargs = many keyword arguments
def profile(**info):
    print(info)

profile(name="Naveen", age=25)
# {'name': 'Naveen', 'age': 25}


#Functions Calling Functions
def square(n):
    return n * n

def print_square(x):
    result = square(x)
    print(result)

    
#Lambda (Anonymous) Functions

def add(x, y):
    return x + y

add = lambda x, y: x + y
print(add(2, 3))                        # Output: 5
'''