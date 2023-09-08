# Important functionalities

import numpy as np

np_array = np.array([5, 10, 15, 20, 25, 30])

dot_product = np.dot(np_array, np_array)

print(dot_product)

# Generating random values

print(np.random.rand(1, 2))

# Low=5, High=15, Size=2. Generate 2 values between 5 and 15 (exclusive)
print("--Random Matrix without shape--")
print(np.random.randint(5, 15, 2))

# Low=5, High=15, Size=(3,2). Generate a matrix of shape (3,2) with values between 5 and 15 (exclusive)
print("--Random Matrix with shape--")
print(np.random.randint(5, 15, (3, 2)))

# Sampling the data
array = np.array([1, 2, 3, 4, 5])

# Sample 10 data points with replacement.
print("--Random Choice with replacement--")
print(np.random.choice(array, 10, replace=True))

# Sample 3 data points without replacement.
print("--Random Choice without replacement--")
print(np.random.choice(array, 3, replace=False))

# Randomly shuffling values
# it can be helpful to randomly shuffle your array. Numpy has a shuffle() function that does just that.

x = [1, 2, 3, 4, 5]  # Create a list of 5 elements
np.random.shuffle(x)  # Randomly shuffle the order of the elements in the list

print("----- Random Shuffle ------")
print(x)

# if you want the random selections to be the same every time, you need to set a seed.

np.random.seed(42)
print(x)
