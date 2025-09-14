import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel"],
    "Age" : [21,23,25,26],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur"],
    "Survived" : [1,0,1,0]
}

df = pd.DataFrame(data)
df.to_json("output.json",index=False)       # Saving output

#Selecting Single Columns:
name=df["Name"]
print(name)

#Selecting Multiple Columns:
name=df[["Name","Age"]]
