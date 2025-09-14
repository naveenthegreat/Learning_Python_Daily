import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel","Rudra","Dev","Praveen"],
    "Age" : [21,23,25,26,25,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur","Tiruvanantapuram","Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

# Adding Data
df["Salary"]=df["Age"] * 1250
print(df)

#df.insert(location,"Column_Name",Data_to_insert)
df.insert(0,"ID",[101,102,103,104,105,106,107])         # Most Prescribed
print(df)
