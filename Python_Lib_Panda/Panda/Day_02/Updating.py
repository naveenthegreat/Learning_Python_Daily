import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel","Rudra","Dev","Praveen"],
    "Age" : [21,23,25,26,25,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur","Tiruvanantapuram","Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

# Updating Any Value
# .loc[]
# df.loc[row_index,"Column_Name"] = new_value
df.loc[0,"Age"] = 24
print(df)

# Updating many value
df["Age"] = df["Age"] * 2
print(df)