#List:

#List is the ordered and changeable collection of items.It can store any data types and even mis data types
#ex."list=[1,"Naveen",True,3.6,["ok","bye"]]



#Slicing List:
# list1 = [1,8,7,2,21,15]
# print(list1[1:4])                       #print items at index 1 to 3,it will not include index 4



'''
List Methods:
     list1 = [1,8,7,2,21,15]

1.list1.sort()           ==>  sort in an ascending order
2.list1.reverse()        ==> reverse the list in descending oreder
3.list1.append(4)        ==> add 4 at the add of the list
4.list1.insert(8,222)    ==> insert 222 in place of the 8
5.list1.pop(3)           ==> will delete the item at index 3 and return its value
6.list1.remove(21)       ==> will remove 21 from the list
7.list1.count(7)         ==> will count 7 occurence
'''



# list of fruits using Index and enumerate():
# fruits=["apple","banana","mango","pineapple","grapes"]

# for item in fruits:
#     print(item)

# for i in range(len(fruits)):                              #Using Index
#     print(i,fruits[i])

# for index,char in enumerate(fruits,start=1):              #using enumerate()
#     print(index,char)

# enum_list=list(enumerate(fruits))                         #it will convert into list of tuples
# print(enum_list)



#Nested List:
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list)
# print(nested_list[1])
# print(nested_list[1][2])



#List Compressions:
#These are concise ways to create a list using a single line of code
# square=[x**2 for x in range(10)]
# print(square)                               #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# evens=[x for x in range(10) if x%2==0]
# print(evens)                                #[0, 2, 4, 6, 8]



