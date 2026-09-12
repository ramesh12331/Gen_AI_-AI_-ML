import numpy as np

# Vectorized Operations
a = np.array([3, 4, 5]) 
b = np.array([6, 7, 8]) 
print(a + b) 
print(a - b) 
print(a * b) 
print(a / b)

# Scalar Operations
arr = np.array([1, 2, 3, 4, 5]) 
print(arr + 10) 
print(arr - 10) 
print(arr * 10) 
print(arr / 10)

# Relational Operators
arr = np.array([1, 2, 11, 4, 2, 3, 1])

print(arr[arr>8])
print(arr[arr < 5])
print(arr[arr == 2])
# Boolean Indexing

arr = np.array([10, 20, 30, 40, 50])

condition = arr>25

print(condition)
print(arr[condition])

# Fancy Indexing
arr = np.array([10, 20, 30, 40, 50])
result = arr[[0, 2, 4]]
print(result)

# 1D Indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2]) 
print(arr[-1])

# 1D Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
print(arr[:3]) 
print(arr[-2:]) 
print(arr[::2])

# 2D Indexing
arr = np.array([ [10, 20, 30], [40, 50, 60] ])
print(arr[0,1])
print(arr[1,2])

# 2D Slicing
arr = np.array([ [10, 20, 30], [40, 50, 60], [70, 80, 90] ])
print(arr[:2])
print(arr[:, :2])
print(arr[1:3, 1:3])

# Mathematical Functions
arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.prod(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# argmin() and argmax()
arr = np.array([10, 5, 30, 2, 50])
print(np.argmin(arr))
print(np.argmax(arr))

# axis
arr =np.array([[10, 20, 30], [40, 50, 60]]) 
result = np.sum(arr, axis=0)
print(result)

result = np.sum(arr, axis=1)
print(result)
# round(), ceil() and floor()
arr = np.array([1.2, 2.7, 3.5, 4.9])

print(np.round(arr))
print(np.ceil(arr))
print(np.floor(arr))

# Dot Product
arr = np.array([ [2, 3], [4, 5] ]) 
a1 = np.array([ [1, 8], [2, 9] ])

result = np.dot(arr, a1)
print(result)