import numpy as np
arr_1=np.array([1,2,3])
arr_2=np.array([[1,2,3],[3,4,5]])
arr_3=np.array([[[1,2,3],[3,4,5],[5,6,7]]])

print(arr_1.ndim)                   # outpu : 1     represent 1d array
print(arr_2.ndim)                   # outpu : 2     represent 2d array
print(arr_3.ndim)                   # outpu : 3     represent 3d array