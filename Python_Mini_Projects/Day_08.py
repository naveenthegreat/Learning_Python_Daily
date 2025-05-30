# # #Student Grade Calculator (Using Functions)

# # def input_user():
    
# #     d1=int(input("Enter yoour marks: "))
# #     d2=int(input("Enter yoour marks: "))
# #     d3=int(input("Enter yoour marks: "))
# #     return d1,d2,d3

# # marks = input_user()
# # # print("Marks Received: ",marks)


# # def tot_avg():
# #     total=sum(marks)
# #     avg=float(total/3)
# #     return total,avg

# # total, avg = tot_avg()  
# # # print("The Total is ",total)
# # # print("The Average is ",avg)

# # def grade(avg):
# #     if avg>=90:
# #         return "A"
# #     elif avg>=75 or avg <=89:
# #         return "B"
# #     elif avg>=70 or avg<=74:
# #         return "C"
# #     elif avg>=40 or avg<=59:
# #         return "D"
# #     elif avg<=40:
# #         return "F"

# #     return avg

# # def show_result(total,avg,grade(avg)):
# #     print("----------Student Result----------")
# #     print("Total is ",total)
# #     print(f"Average is {avg:.2f}")
# #     print(f"Grade is {grade(avg)}")

# # result=show_result(total,avg,grade(avg))
# # print(result)

# # Student Grade Calculator (Using Functions)

# def input_user():
#     d1 = int(input("Enter your marks for Subject 1: "))
#     d2 = int(input("Enter your marks for Subject 2: "))
#     d3 = int(input("Enter your marks for Subject 3: "))
#     return d1, d2, d3

# def tot_avg(marks):
#     total = sum(marks)
#     avg = total / len(marks)
#     return total, avg

# def grade(avg):
#     if avg >= 90:
#         return "A"
#     elif 75 <= avg < 90:
#         return "B"
#     elif 60 <= avg < 75:
#         return "C"
#     elif 40 <= avg < 60:
#         return "D"
#     else:
#         return "F"

# def show_result(total, avg, grade_letter):
#     print("\n---------- Student Result ----------")
#     print(f"Total: {total}")
#     print(f"Average: {avg:.2f}")
#     print(f"Grade: {grade_letter}")

# # DRIVER CODE
# marks = input_user()
# total, avg = tot_avg(marks)
# grade_letter = grade(avg)
# show_result(total, avg, grade_letter)



#Personal Expense Tracker (Function-Powered)

expenses=[]

def menu():
    print("\n1. Add Expense\n2. View Total\n3. View by Category\n4. Highest Expense\n5. View All\n6. Exit")
    return int(input("\nChoose the option: "))

def add_expense():
    amount=int(input("\nEnter Amount: "))
    category=input("Enter Catergory: ")
    expenses.append({"Amount": amount,"Category":category})
    print("Expenses Added")

def view_total():
    total=sum(entry["Amount"] for entry in expenses)
    print(f"Total spending:{total}\n")

def view_by_category():
    cat=input("\nEnter category to filter: ")
    found=False
    for entry in expenses:
        if entry["Category"].lower() == cat.lower():
            print(entry)
            found = True
    if not found:
        print("No expenses found in these category.\n")

def view_max():  # ✅ Clear, safe, and descriptive

    if not expenses:
        print("No expenses")
        return
    max_entry=max(expenses,key=lambda x:x["Amount"])
    print(f"\nHighest Expenses -> Amount: {max_entry['Amount']}, Category: {max_entry['Category']}")
   
def view_all():
    print(expenses)

def menu1():

    while True:    
        choice=menu()

        if  choice==1:
         add_expense()

        elif choice==2:
         view_total()
        
        elif choice==3:
         view_by_category()
 
        elif choice == 4:
         view_max()

        elif choice==5:
         view_all()

        elif choice==6:
         print("Goodbye! 👋\n")    
         break

        else:
         print("Invalid Entered")
        
menu1()
