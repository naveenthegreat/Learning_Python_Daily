#Loops
#1
# n=int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} x {i} ={n*i}")

#2
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#      print(f"Hello {name}")

#3 solving 1 by while loop
# n=int(input("Enter a number: "))
# i=1
# while (i<11):
#     print(f"{n} x {i}= {n*i}")
#     i+=1


#4
# n=int(input("Enter a number: "))

# for i in range (2,n):
#     if (n%2)==0:
#         print("The no is not prime")
#         break

#     else:
#         print("The no is prime")
        

#5
# n=int(input("Enter the number: "))
# i=1
# sum=0

# while (i<=n):
#     sum +=i
#     i+=1

#     print(sum)


#6
# n=int(input("Enter the number: "))
# product=1

# for i in range (1,n+1):
#     product = product*i

# print(f"The factorial of {n}: {product}")

    
# #7 star pattern
# n=int(input("Enter the number: "))
# for i in range (1,n+1):
#     print(" " * (n-i),end="")
#     print("*"* (2*i-1),end="")
#     print("")

#8
'''
*
**
***
'''
# n=int(input("Enter the number: "))
# for i in range (1,n+1):
#     print(" " * (n-i))
#     print("*"* (i),end="")
#     print("")

'''
***
* *
***
'''
# n=int(input("Enter the number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"* n)

#     else:
#         print("*",end="")
#         print(" "* (n-2), end="")
#         print("*",end="")
#     print("")
# n = int(input("Enter the number: "))

# for i in range(1, n + 1):
#     if i == 1 or i == n:
#         print("*" * n)  # full row of stars
#     else:
#         print("*" + " " * (n - 2) + "*")  # hollow row: star, spaces, star


#10
# n = int(input("Enter the number: "))
# for i in range (1,11):
#     print(f"{n} x {11-i} = {n*(11-i)}")    