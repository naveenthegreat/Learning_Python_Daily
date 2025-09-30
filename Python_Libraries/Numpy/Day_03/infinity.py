# np.isinf(array)
import numpy as np
arr = np.array([1,2,np.inf,-np.inf])
print(np.isinf(arr))

print(np.nan_to_num(arr, posinf=1020, neginf=-1299))