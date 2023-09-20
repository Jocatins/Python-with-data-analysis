# There are a few ways to fill in missing values.

# Using a statistical value

import numpy as np
import pandas as pd

pd_series = pd.Series([5, 10, np.nan, 15, 20, np.nan, 25, 50, np.nan])

print("Average of non-missing values: {0}".format(pd_series.mean()))

pd_series = pd_series.fillna(pd_series.mean())
print("fillna applied", pd_series)

# Above, we created a Pandas series, which is just a single column of a Pandas dataframe.
# Within our series, we added 3 missing values with np.nan.

# Pandas allows you to easily fill in missing values with the fillna() function.
# We pass this function the value we want to use. In this example, we pass the mean of the values that are not missing

# Pandas also makes it easy to drop missing values using the dropna() function:

# Drop rows with missing data
pd_series = pd_series.dropna()
print("drop-missing data", pd_series)

# Or you can find which values are missing with the isnull() function.

# Show which rows are missing
print(pd_series.isnull())
