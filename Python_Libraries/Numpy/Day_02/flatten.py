'''
.ravel -> view
.flatten -> copy
'''
import numpy as np

arr=np.array([[1,2,3],[3,4,5]])
print(arr.ravel())
print(arr.flatten())