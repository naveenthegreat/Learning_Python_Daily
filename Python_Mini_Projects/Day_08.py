# #Student Grade Calculator (Using Functions)

# def input_user():
    
#     d1=int(input("Enter yoour marks: "))
#     d2=int(input("Enter yoour marks: "))
#     d3=int(input("Enter yoour marks: "))
#     return d1,d2,d3

# marks = input_user()
# # print("Marks Received: ",marks)


# def tot_avg():
#     total=sum(marks)
#     avg=float(total/3)
#     return total,avg

# total, avg = tot_avg()  
# # print("The Total is ",total)
# # print("The Average is ",avg)

# def grade(avg):
#     if avg>=90:
#         return "A"
#     elif avg>=75 or avg <=89:
#         return "B"
#     elif avg>=70 or avg<=74:
#         return "C"
#     elif avg>=40 or avg<=59:
#         return "D"
#     elif avg<=40:
#         return "F"

#     return avg

# def show_result(total,avg,grade(avg)):
#     print("----------Student Result----------")
#     print("Total is ",total)
#     print(f"Average is {avg:.2f}")
#     print(f"Grade is {grade(avg)}")

# result=show_result(total,avg,grade(avg))
# print(result)

# Student Grade Calculator (Using Functions)

def input_user():
    d1 = int(input("Enter your marks for Subject 1: "))
    d2 = int(input("Enter your marks for Subject 2: "))
    d3 = int(input("Enter your marks for Subject 3: "))
    return d1, d2, d3

def tot_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

def grade(avg):
    if avg >= 90:
        return "A"
    elif 75 <= avg < 90:
        return "B"
    elif 60 <= avg < 75:
        return "C"
    elif 40 <= avg < 60:
        return "D"
    else:
        return "F"

def show_result(total, avg, grade_letter):
    print("\n---------- Student Result ----------")
    print(f"Total: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade_letter}")

# DRIVER CODE
marks = input_user()
total, avg = tot_avg(marks)
grade_letter = grade(avg)
show_result(total, avg, grade_letter)



#Personal Expense Tracker (Function-Powered)
