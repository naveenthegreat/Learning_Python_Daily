import pandas as pd
import os
df=pd.read_csv(r"C:\Users\NAVEEN\OneDrive\Desktop\Python_Project\Learning_Python_Daily\Python_Libraries\Panda\Day_01\netflix_titles.csv",encoding="latin1")

print("\nShape of columns:",df.shape)               # (rows,columns)
print("\ncolumns: ",df.columns)                     # Lists of columns
print("\n",df.info())
print("\n")
print(df.isnull())                                  # Missing value


# Basic Exploration
print("\n")
print(df["type"].unique())                  # uniue values : 'Movie' & 'TV Show'
print("\n")
print(df["type"].value_counts())            # Count of 'Movie' & 'TV Show'
print("\n")
print("Oldest: ",df['release_year'].min())
print("Newest: ",df['release_year'].max())

#print(os.getcwd())                         # current woking diretory               # additional practice