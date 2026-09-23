# ============================================================
# BROADCASTING
# ============================================================


# ============================================================
# 13. BROADCASTING - BASIC EXAMPLE
# ============================================================

# a shape = (4, 3)
# b shape = (3,)
#
# NumPy broadcasts b across every row of a.

a = np.arange(12).reshape(4, 3)

b = np.arange(3)

print("\nShape of a:")
print(a.shape)

# Output:
# (4, 3)

print("\nShape of b:")
print(b.shape)

# Output:
# (3,)

print("\nArray a:")
print(a)

# Output:
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

print("\nArray b:")
print(b)

# Output:
# [0 1 2]

print("\nBroadcasting Addition:")
print(a + b)

# Output:
# [[ 0  2  4]
#  [ 3  5  7]
#  [ 6  8 10]
#  [ 9 11 13]]

# =================
# ============================================================
# 14. BROADCASTING - INCOMPATIBLE SHAPES
# ============================================================

a = np.arange(12).reshape(3, 4)

b = np.arange(12).reshape(4, 3)

print("\nShape of a:")
print(a.shape)

# Output:
# (3, 4)

print("\nShape of b:")
print(b.shape)

# Output:
# (4, 3)


# This produces a ValueError:
#
# print(a + b)

# Error:
# ValueError:
# operands could not be broadcast together

# ==========================================
# ============================================================
# 15. BROADCASTING EXAMPLE
# ============================================================

a = np.arange(3).reshape(1, 3)

b = np.arange(3).reshape(3, 1)

print("\nShape of a:")
print(a.shape)

# Output:
# (1, 3)

print("\nShape of b:")
print(b.shape)

# Output:
# (3, 1)

print("\nBroadcasting Result:")
print(a + b)

# Output:
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

# ====================
# ============================================================
# 16. ANOTHER BROADCASTING EXAMPLE
# ============================================================

a = np.arange(12).reshape(4, 3)

b = np.arange(3)

print("\nShape of a:")
print(a.shape)

# Output:
# (4, 3)

print("\nShape of b:")
print(b.shape)

# Output:
# (3,)

print("\nResult:")
print(a + b)

# Output:
# [[ 0  2  4]
#  [ 3  5  7]
#  [ 6  8 10]
#  [ 9 11 13]]

# =================
