# Numpy is a fast and efficient library for storing and manipulating data - usually through array data structures (which are similar to Python lists).

import numpy as np

# Single dimensional arrays
# This creates our array
np_array = np.array([5, 10, 15, 20, 25, 30])
print("--0--")

# Gets the unique values
print(np.unique(np_array))
print("--1--")

# Calculates the standard deviation
print(np.std(np_array))
print("--2--")

# Calculates the maximum
print(np_array.max())
print("--3--")

# Squares each value in the array
print(np_array ** 2)
print("--4--")

# Adds the arrays together element wise
print(np_array + np_array)
print("--5--")

# The sum of the squares of the elements
print(np.sum(np_array ** 2))
print("--6--")

# Gives you the shape: (rows, columns)
print(np_array.shape)

# Two dimensional arrays

# You will also want to understand how to use 2D arrays, arrays that have both rows and columns.
# This is typically how you would represent a matrix of data using numpy.


# Create 2d array
print("--Two dimensional Array--")
np_2d_array = np.array([[1, 2, 3],
                        [4, 5, 6]])
print(np_2d_array)

# Calculate the transpose, which is when you swap the columns and rows.
print("--1--")
np_2d_array_T = np_2d_array.T
print(np_2d_array_T)

# Print the shape of the array as (number of rows, number of columns)
print("-------------2-----------")
print(np_2d_array.shape)

# Access elements in the 2d array by index.
# First index is the row number
# Second index is the column number
# Index numbers start from 0
print("-------------3--------------")
print(np_2d_array[1, 1])
print(np_2d_array[0, 2])

# Important functionalities
