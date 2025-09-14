# Sorting 1 column
# df.sort_values(by="Column_Name",ascending=True/False,inplace=True)   ....True/False : ascending/descending

import pandas as pd
data = {
    "Name" : ["Naveen", "Kumar","Nayak"],
    "Age" : [23,29,22],
    "Salary" : [20000,15000,74000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age",ascending=True,inplace=True)
print(df)

df.sort_values(by="Age",ascending=True,inplace=True)
print(df)

print("\n")

# For multiple Columns sorting
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
print(df)