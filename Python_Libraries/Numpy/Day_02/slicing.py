'''
arr.np[start:stop:step]
arr.np[start:end]
'''
import numpy as np

arr = np.array([12,21,22,33,45])
print(arr[:4])
print(arr[1:3:2])
print(arr[::2])
print(arr[:3:])
print(arr[::-1])