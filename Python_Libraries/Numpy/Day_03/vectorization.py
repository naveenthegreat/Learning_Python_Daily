'''
🔹 What is Vectorization?
    Vectorization is the process of replacing slow, repetitive loops in Python with fast, 
    optimized operations that work on entire arrays at once (using NumPy).
'''
import time

nums = [1, 2, 3, 4, 5]

# Without vectorization (loop)
start = time.time()
result = []
for x in nums:
    result.append(x + 10)
end = time.time()

print("Result:", result)
print("Time taken:", end - start)


import numpy as np
import time

nums = np.array([1, 2, 3, 4, 5])

# With vectorization
start = time.time()
result = nums + 10
end = time.time()

print("Result:", result)
print("Time taken:", end - start)
