import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel"],
    "Age" : [21,23,25,26],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur"],
    "Survived" : [1,0,1,0]
}

df = pd.DataFrame(data)
print(df)

##Lets Save it in 3 different types of file:
# df.to_csv("output.csv",index=False)     #index=false = file will not include extra column "0,1,2"
# df.to_excel("output.xlsx",index=False)
# df.to_json("output.json",index=False)

##Let Read the file into a DataFrame
# df=pd.read_csv("output.csv", encoding="latin1")  #if u get UnicodeDecodeError then use it also ="utf-8"
# print(df)
##Same for other types of files
