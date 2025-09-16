# Creating arrays from python list
# np.array([ele1, ele2, ele3])
import numpy as np
lists= np.array([1,2,3,4,5])                # list to array 
print(lists)

# with default values
# np.zeros(shape) like (2) for 1d, (2,2) for 2d             for zeros
arr= np.zeros(3)
print(arr)

#np.ones(shape)                                             for ones 
arr_= np.ones(3)
print(arr_)

# full(shape,value)                                         for any value
arr__=np.full((3,3),5)
print(arr__)