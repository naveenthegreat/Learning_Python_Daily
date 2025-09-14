# Removing column keeps data clean and focus

import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel","Rudra","Dev","Praveen"],
    "Age" : [21,23,25,26,25,25,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur","Tiruvanantapuram","Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

# df.drop(columns=["Column_Name"], inplace = True)
df.drop(columns=["Survived","City"], inplace=True)
print(df)