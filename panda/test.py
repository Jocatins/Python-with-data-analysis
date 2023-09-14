# The task is fairly simple, you just have to read the dataset, and return its shape.

import pandas as pd  # calling pandas module


def read_csv():  # function read_csv
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower",
             "weight", "acceleration", "model_year", "origin", "car_name"]

    df = pd.read_csv("auto-mpg.data", header=None,
                     names=names, delim_whitespace=True)
    return df.shape


print(read_csv())


# On line 11
# path: The path to the dataset
# header: In case the columns are provided explicitly, it’s set to None.
# names: List of columns’ names to be used
# delim_whitespace: Specifies whether or not whitespace should be used as a sep

# At line 13, we are returning shape, a property of the dataframe df.

# at line 16, where we are calling the function read_csv().

# For this dataset, the function will return (398, 9) as there are 398 rows and 9 columns.
