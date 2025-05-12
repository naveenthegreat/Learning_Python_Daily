#Smart To-Do List App (Console-Based)

list=[]

while True:
    print("\n----------To Do Menu----------\n")
    print("1. Add Task\n2. View Tasks\n3. Delete \n4. Exit")

    num=int(input("Enter Task No.: "))

    if num==1:
      add_task=input("Task Name: ")
      list.append(add_task)
      print("Task Added\n\n")
      continue

    elif num==2:
      for index,value in enumerate(list,start=1):
        print(index,value)
      continue

    elif num==3:
       n=int(input("Enter The Number of Task: "))
       list.pop(n)
       continue

    

    elif num==4:
       break

    else:
       print("You Entered Invalid")
