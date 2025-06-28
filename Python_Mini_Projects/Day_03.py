username="Naveen"
passwd="naveen@123"

c=input("Enter the Username:")
d=input("Enter the Password:")

if c==username and d==passwd:
    print("Access Granted")
    print("Welcome Naveen!!!")

elif c==username and d!=passwd:
    print("Wrong Password")

elif c!=username and d==passwd:
    print("Wrong Username")

else :
    print("Access Denied")