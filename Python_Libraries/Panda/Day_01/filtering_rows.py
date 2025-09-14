import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel","Rudra","Dev","Praveen"],
    "Age" : [21,23,25,26,25,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur","Tiruvanantapuram","Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

high_age=df[df["Age"] > 23]
print(high_age)

print("\n\n")

#filtering rows 
filtered=df[(df["Age"] > 30) & (df["Survived"] > 0)]        # this "|" also can be use
print(filtered)
