'''
df.["column_name"].mean()
df.["column_name"].sum()
df.["column_name"].min()
df.["column_name"].max()
'''

import pandas as pd
data = {
    "Name" : ["Naveen", "Kumar","Nayak"],
    "Age" : [23,29,22],
    "Salary" : [20000,15000,74000]
}

df = pd.DataFrame(data)

avg_salary=df["Salary"].mean()
print(avg_salary)
