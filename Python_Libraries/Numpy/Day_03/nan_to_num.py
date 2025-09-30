# np.nan_to_num(array,nan=value)
import numpy as np
arr = np.array([1,2,33,np.nan,23,np.nan])
print(np.nan_to_num(arr, nan=1))
