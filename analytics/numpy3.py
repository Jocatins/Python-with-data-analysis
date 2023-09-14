from scipy import stats
import numpy as np


# Create a function which takes that numpy 1-D array as input and returns the following (in the same order as listed):

# Max - Maximum value in the array
# Std - Measure of variation between the elements of an array
# Sum - Value obtained as a result of adding all the elements of an array
# Dot product - Inner product of the vectors

def perform_calc(array):

    np_array = np.array()

    print(np_array.max())

    return np.max(array), np.std(array), np.sum(array), np.dot(array, array)

# Create a function that takes in two numpy 1-D arrays and returns the correlation and p-value as a tuple.


# def correlation(array1, array2):
#     return stats.pearsonr(array1, array2)

# calling the function and printing result
# print(correlation(np.random.rand(5),np.random.rand(5)))
