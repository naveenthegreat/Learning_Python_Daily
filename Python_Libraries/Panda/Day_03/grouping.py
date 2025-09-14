import pandas as pd
data = {
    "Name" : ["Naveen", "Kumar","Nayak","Krishna"],
    "Age" : [23,29,23,32],
    "Salary" : [20000,15000,74000,34000]
}

df = pd.DataFrame(data)

grouped=df.groupby("Age")["Salary"].sum()      # mean, max, min, count, std
print(grouped)