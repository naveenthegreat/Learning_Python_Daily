#mini challenge
n=input("Enter the password: ")
lenght=len(n)
for i in (1,n):
    if lenght<4:
        print("💀 Too Weak\n","*"*lenght,end="")
        break
    elif lenght>4 or lenght<7:
        print("🟡 Moderate\n","*"*lenght,end="")
        break
    else :
        print("🟢 Strong\n","*"*lenght)