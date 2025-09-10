import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel",None,"Dev","Praveen"],
    "Age" : [21,23,25,26,None,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur",None,"Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,None,0,1]
}

df = pd.DataFrame(data)

# Fill missing values : 
# fillna() 
# df.fillna(value,inplace = True)
df.fillna(0,inplace=True)
df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Age"]=df["Age"].fillna("Singapore")
print(df)