#Dictionaries
'''
Dictionary is the collection of key-value pairs, where each key is unique and maps to value.
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys.

#Creating Dictionary
d={}                                        ==> An empty dictionary
d={"a":1,"b":2}                             ==> A standard way
d=dict(name="Naveen",age=25)                ==> Using dict() constructor

user={"name":"Naveen","age":25}
print(user["name"])

user["name"]="Nayak"                        ==> these will update
user["email"]="Nayak44@"                    ==> if no email key then it will add in it

#Dictionary Methods:
        l={"Name":"Naveen","age":23,"Mobile":"Oppo A25"}
1. l.get(key)                               ==> return value or none if no found           
2. l.keys()                                 ==> returns a list of keys
3. l.values()                               ==> returns a list of values
4. l.items()                                ==> returns a list of (key,value) tuples
5. l.pop(keys)                              ==> remove keys and return value
6. l.update(dict2)                          ==> adds or update keys-values from dict2
7. l.clear()                                ==> removes everything from 

#Looping to dictionaries

for key, value in user.items():
    print(f"{key}: {value}")

#Nesting Dictionaries

users = {
    "user1": {"name": "Naveen", "age": 25},
    "user2": {"name": "Arjun", "age": 30}
}
print(users["user2"]["name"])   # Arjun

#Dictionary Compression

squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

'''
''' Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!'''
# d={"Naam":"Name","Sahi":"correct","Achha":"Good"}
# ds=input("Enter a name: ")
# print(d[ds])

'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''
# s={}
# k1=input("Enter your name: ")
# k2=input("Enter your language: ")
# s.update({k1: k2})

# k1=input("Enter your name: ")
# k2=input("Enter your language: ")
# s.update({k1: k2})

# k1=input("Enter your name: ")
# k2=input("Enter your language: ")
# s.update({k1: k2})

# print(s)

