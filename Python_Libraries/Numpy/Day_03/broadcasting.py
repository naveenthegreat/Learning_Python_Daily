'''
What is Broadcasting?
    👉 Broadcasting means NumPy automatically stretches smaller arrays to match the shape of 
        larger arrays so they can work together in operations.
       Instead of writing loops or copying data manually, NumPy handles it for you.
       
🌟 Real-Life Analogy

Imagine:
    You have a cake with multiple slices (big array 🍰).
    You want to sprinkle sugar (small array or a single number) on every slice.
        👉 Do you sprinkle each slice one by one? No! You just shake the sugar jar, and it falls equally on all slices at once.

That’s broadcasting: a small thing automatically applied to all big things.
'''
import numpy as np
arr = np.array([1200,200,2300])
print(arr - (arr * 10/100))

A = np.array([1,2,34])
B = np.array([12,23,33])
print(A+B)

C = np.array([100])
print(A+C)

arr_ = np.array([[1,2,3],[4,5,6]])
arr__ = np.array([1,2,3])
print(arr_+(arr_.reshape(2,3)))
'''
Why is Broadcasting Useful?

    Removes the need for manual loops
    Saves memory (doesn’t actually copy data, just pretends to)
    Super fast because operations happen in C-level vectorized code
'''