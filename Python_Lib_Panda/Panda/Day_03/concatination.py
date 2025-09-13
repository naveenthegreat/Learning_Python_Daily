# df.concat([df1,df2],axis=0,ignore_index=True)
import pandas as pd

df_region_1=pd.DataFrame({
    "Customer_id" : [1,2],
    "Name" : ["Naveen","Kumar"]
})

df_region_2=pd.DataFrame({
    "Customer_id" : [3,4],
    "Name" : ["Vinayak","Nayak"]
})

df_concate=pd.concat([df_region_1,df_region_2],axis=0,ignore_index="True")
print(df_concate)

print("\n")

df_concate=pd.concat([df_region_1,df_region_2],axis=1,ignore_index="True")
print(df_concate)