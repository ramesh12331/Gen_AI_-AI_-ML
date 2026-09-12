import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)

# 3. Python List vs NumPy Array
list_1 = [1, 2, 3] 
list_2 = [4, 5, 6]
print(list_1 + list_2)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)

# 4. Creating a NumPy Arra
arr = np.array([3,4,5])
print(arr)

numbers = [10, 20, 30, 40]

arr = np.array(numbers)
print(arr)

# 1D Array
arr = np.array([1,2,3,4,5])
print(arr)

# 2D Array
print("2D Array")
arr = np.array([
    [1, 2, 3], 
    [4, 5, 6]
])

print(arr.ndim)

# 3D Array
arr = np.array([
    [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ]
])

print(arr.ndim)

# 6. Array Attributes
arr = np.array([
    [1, 2, 3], [4, 5, 6]
])

print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# Element-wise Operation
a = np.array([3, 4, 5])
b = np.array([6,7,8])

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# ➕ Adding a single number
arr = np.array([10, 20, 30, 40])
print(arr+5)

# dtype

arr = np.array([45, 67, 899874564675, 23], dtype="int64")
print(arr.dtype)

# NumPy is Usually Homogeneous
arr = np.array([34, 56, 78, 23, 45.7])
print(arr)
print(arr.dtype)

# Ones and Zeros
arr = np.ones((3,4))
print(arr)

arr = np.zeros((3,4))
print(arr)

# Identity Matrix
arr = np.eye(4)
print(arr)

print("Identity Matrix")
arr = np.identity(5)
print(arr)

# Diagonal Matrix

arr = np.diag([2,3,4,5,6])
print(arr)

# Empty Array
arr = np.empty([2,4])
print(arr)

# arange()

arr = np.arange(2, 10, 2)
print(arr)

arr = np.arange(100, 10, -10)
print(arr)

# linspace()
arr = np.linspace(1, 10, 9)
print(arr)

# Random Arrays
arr = np.random.rand(4,5)
print(arr)

# Reshape
arr = np.arange(1, 7) 
print(arr)
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)

# Flatten
arr = np.array([ [1, 2, 3], [4, 5, 6] ]) 
flattened = arr.flatten()
print(flattened)

# Ravel
arr = np.array([ [1, 2, 3], [4, 5, 6] ]) 
raveled = arr.ravel() 
print(raveled)

# Transpose

arr = np.array([ [1, 2, 3], [4, 5, 6] ]) 
print(arr.T)

# View vs Copy
arr = np.array([1, 2, 3]) 
arr_view = arr.view() 
arr_copy = arr.copy()

print(arr_view)
print(arr_copy)