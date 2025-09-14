import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel",None,"Dev","Praveen"],
    "Age" : [21,23,25,26,None,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur",None,"Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,None,0,1]
}

df = pd.DataFrame(data)

# Renaming Columns
df.rename(columns={"Survived":"_Survived_"},inplace=True)
print(df)

print("\n")

# Replacing Values
df["City"] = df["City"].replace({"Tiruvanantapuram" : "Tiru"})
print(df)