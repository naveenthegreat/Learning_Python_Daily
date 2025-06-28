#print profile info
print("\n\n---------------- User Profile -----------------\n")
print("Name: ",n)
print("Age: ",ag)
print("Height: ",height)
print("Is Student?",is_student)

#formatted version
print(f"\n\n{n} is {ag} years old and {height} feet tall. Student Status: {is_student}\n\n")


#2nd project: User Profile by taking input from user

print("\n\n---------------- User Profile -----------------\n")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height: "))
stu=input("Are you a student? (Yes/No): ").lower()

print(f"\n\nMy name is {name} and i am {age} years old\n\n")
print(f"Student Status: ",stu)