import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel"],
    "Age" : [21,23,25,26],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur"],
    "Survived" : [1,0,1,0]
}

df = pd.DataFrame(data)
df.to_json("output.json",index=False)       # Saving output

# To view Rows in a dataset:
df=pd.read_json("output.json")
print(df.head(2))           # display first 2 rows
print(df.tail(2))           # display last 2 rows
print(df.info())              # column types + null values
print(df.shape)               # (rows,columns)
print(df.describe())          # statistics (mean, std, min, max)       
print(f'Column Names: \n{df.columns}')  # Will display index and datatype

