# #Tuples and Sets

# #Tuples
# '''
# Tuple is ordered and immutable collection of items.It also contains mixed data types as list.

# #list to tuple:
#    t=tuple([1,2,3])

# #why tuples?
#    Used for mixed data, immutable(safe from accidental changes), 
#    faster than list(Contains less memory), can be used as dictionary keys

# #Methods of Tuples:
# t.count(2)                  ==> it counts how many time 2 occur
# t.index(2)                  ==> it will return the index of 2  i.e. 1

# '''

# #Sets
# '''
# Set is unordered, unindexed collection of unique elements.No Duplicates and No indexing(no set(0)).

#     Why?
# ==> Extremely fast membership tests: if x in set, Automatically removes duplicates,
#     Great for mathematical set logic, No duplicates allowed


    
# s = {}         # This is a dictionary!
# s = set()      # This is an empty set 


# # s1 = {1, 2, 3}
# # s2 = set([3, 4, 5])
# # s3 = set("hello")      # {'h', 'e', 'l', 'o'} — only unique letters
# # print(s1,s2,s3)


# #Set Methods:
#                      list={1,2,3,33,45}

# 1. list.add(23)                         ==> add an element
# 2. list.remove(2)                       ==> item 2 will remove 
# 3. list.discard(22)                     ==> if 22 isn't then it will not display "Error"
# 4. list.pop()                           ==> remove random item
# 5. list.update( {4,5},[34] )            ==> add elements 1 or more iterables(eg.lists,sets)
# 6. list.copy()                          ==> returns a copy of set


# #Set Operations:
# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A | B)                 # Union → {1, 2, 3, 4, 5}
# print(A & B)                 # Intersection → {3}
# print(A - B)                 # Only in A → {1, 2}        ... Difference
# print(A ^ B)                 # In A or B but not both → {1, 2, 4, 5}   ...Symmetric_Difference


# '''
# #Can we have a set with 18 (int) and '18' (str) as a value in it?
#  set={18,'18'}
# print(set)                             ==>The ans is yes bcoz 18 is int and '18' is string

# # Can you change the values inside a list which is contained in set S?
#  s = {8, 7, 12, "Harry", [1,2]}
#  print(s)                               ==> list can't be include in set
#  print(set.insert[5,2])

# #What will be the length of following set s:
#  s = set()
#  s.add(20)
#  s.add(20.0)
#  s.add('20')
#  print(s)
#  print(len(s))               #The len will be 2 bcoz 1==1.0