# # Using f-strings as formated output
# name="Naveen"     #'name' is a variable that stores the value 'Naveen'
# age=25            # variables can store multiple values and whatever data types such as int,bool,float,string 
# print(f"My name is {name} and my age is {age}")

# #let's create a simple project: "User Profile"


# #user profile generator
# n="Naveen"        #string
# ag=25           #int
# height=5.9      #in feet and float
# is_student=True #boolean


# #print profile info
# print("\n\n---------------- User Profile -----------------\n")
# print("Name: ",n)
# print("Age: ",ag)
# print("Height: ",height)
# print("Is Student?",is_student)

# #formatted version
# print(f"\n\n{n} is {ag} years old and {height} feet tall. Student Status: {is_student}\n\n")


#2nd project: User Profile by taking input from user

print("\n\n---------------- User Profile -----------------\n")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height: "))
stu=input("Are you a student? (Yes/No): ").lower()

print(f"\n\nMy name is {name} and i am {age} years old\n\n")
print(f"Student Status: ",stu)
