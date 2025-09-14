# Interpolate :
'''
 A way to fill missing values by "guessing" them based on surrounding values.

 For ex.: 10,20,30,,50 then it will guess 40

 It guesses the value by formula: y=y1 + (x2-x1) x (y2-y1)
                                         (x-x1)

Here:

x1=1,y1=60 (Day 1, Weight 60)
x2=3,y2=62 (Day 3, Weight 62)
x=2 (Day 2, missing)

Plugging in:

y=60 + {(2-1)/(3-1)}x (62-60)=61

👉 So Day 2 = 61 (the midpoint).
'''

# Advantages : 
'''
i. Keeps trends smooth - if your data is like a time series (stock price, weather, sensor data),
   interpolation maintains the flow.

ii. Better than random guesses - it uses actual data around the gap to make a logical 
    estimate.

iii. Essential in ML preprocessing - models can't handle missing values, and interpolation 
     gives more realistic replacements.
'''

import pandas as pd
data = {
    "Name" : ["Naveen", "Nayak", "Krishna", "Princel","Rudra","Dev","Praveen"],
    "Age" : [21,22,None,24,25,26,38],
    "City" : ["Tokyo", "Sinapore", "Lucknow", "Mirzapur","Tiruvanantapuram","Tiruvanantapuram","Chennai"],
    "Survived" : [1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)
print("Before Interpolation")
print(df)

df["Age"]=df["Age"].interpolate(method="linear")
print("After interpolation")
print(df)

# When to use :
'''
i.   Time series Data (temperature, stock prices, daily sales)
ii.  Continuous Data (heights, weights, measurements)
iii. When you believe that missing value should follow the trend of nearby values.
'''

# Other methods:
'''
Sometimes data isn’t linear (not straight). Pandas offers:

method='linear' (default) →             straight-line guess (most common).
method='time' →                         good for time series; uses actual time differences.
method='polynomial' (e.g., degree=2) →  fits a curve instead of a straight line.
method='spline' →                       fits a smooth curve (good for wavy data like temperature).
method='pad' / ffill →                  just copies the last known value.
method='bfill' →                        copies the next known value
'''