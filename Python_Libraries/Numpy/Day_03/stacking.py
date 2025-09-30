'''
arranging array as vertical or horizontal
'''
import numpy as np
arr = np.array([[1,2,3],[2,4,5]])
arr_ = np.array([[23,33,445],[22,67,7]])
print(np.vstack((arr,arr_)))
print(np.hstack((arr,arr_)))