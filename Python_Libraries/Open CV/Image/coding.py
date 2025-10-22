import numpy as np

w = np.array([1,2,3])
b = 0
x = np.array([10,20,25])

f = w[0] * x[0] + w[1] * x[1] + w[2] * x[2] 

f = np.dot(w,x) + b

print(f)