#Mini Challenge: Unique Words Analyzer

l=input("\nEnter Your Sentence: ")
print(l)

l2=str.split(l)
l1=tuple(l2)
print("\nOriginal Words: ",l1)

l3=set(l1)
print("Unique Words: ",l3)


print("Total Unique Words: ",len(l3))




