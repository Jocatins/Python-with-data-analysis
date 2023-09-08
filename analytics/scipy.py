# Scipy is a Python library for scientific computing

# A correlation is a numerical measure of the statistical relationship between two variables.
# For us, those variables will usually be two columns of data, for example, the temperature outside and the likelihood of rain.

# One way to calculate the correlation between two vectors of data is with Pearson’s r-value.

# This value ranges between -1 and 1. Where -1 means there is a total negative correlation, 0 means no correlation, and 1 means total positive.

from scipy import stats
import numpy as np

array_1 = np.array([1, 2, 3, 4, 5, 6])
array_2 = array_1

print(stats.pearsonr(array_1, array_2))
