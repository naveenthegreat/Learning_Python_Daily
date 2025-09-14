import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel",None,"Dev","Praveen"],
    "Age" : [21,23,25,26,None,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur",None,"Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,None,0,1]
}

df = pd.DataFrame(data)

'''
Whenever there is missing values in data it represent in 2 ways: 
i.  NaN (Not a Number)
ii. None (for object data types)

'''

# Detecting missing values : isnull()
# isnull() : will return bollean i.e. True (NaN is missing) & False (value is not missing, value is present)

df.isnull()
print(df.isnull())              # True where value is missing
print(df.isnull().sum())        # count missing values per column
print(df.dropna())              # remove the rows with NaN

