# np.delete(array, index, axis=None)

import numpy as np
arr = np.array([12,12,23,34,4])
print(np.delete(arr,0,axis=None))

arr_2d = np.array([[2,3,4],[2.3,33,45]])
print(arr_2d)
print(np.delete(arr_2d,0,axis=0))