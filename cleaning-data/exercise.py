# We will create an additional function outlier_detection that takes a data frame df and returns 2 numbers in a list:

# The 90th percentile for every column
# The 10th percentile for every column

import pandas as pd


def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower",
             "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("auto-mpg.data", header=None,
                     names=names, delim_whitespace=True)
    return df

# Removing outliers from the data


def outlier_detection(df):
    df = df.quantile([.90, .10])
    return df


print(outlier_detection(read_csv()))

# the outlier_detection(df) function at line 21. It takes one arguments as input:

# Line 22 is the most important line. We are using a built-in function quantile()on df which takes one argument:[.90, .10].
# We are specifying the range for quartile that it should be between 0.90 and 0.10.

# At line 26 we are calling the function outlier_detection(read_csv()). First control will transfer to read_csv() at line 9 and we’ll get a dataframe.
# Then control will go to line 11 and 90th and 10th percentile will be returned for each column.
