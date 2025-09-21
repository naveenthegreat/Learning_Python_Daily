"""
np.array(array_name,index,value,axis)
"""
import numpy as np
arr_1d = np.array([10,23,33,45,55,667,34.5])
# new_arr = np.array(arr_1d,2,33.44)
print(np.insert(arr_1d,2,33.44))

arr_2d = np.array([[1,2,3],[4,5,6]])
print(np.insert(arr_2d,1,[8,9,10], axis=0))