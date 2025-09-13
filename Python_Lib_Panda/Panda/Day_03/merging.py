import pandas as pd

df_customers=pd.DataFrame({
    "customer_id" : [1,2,3],
    "Salary" : [20000,34000,43000]
})

df_orders=pd.DataFrame({
    "customer_id" : [1,2,4],
    "Order_amt" : [230,340,330]
})

df_merged=pd.merge(df_customers,df_orders,on="customer_id",how="outer")
print(df_merged)