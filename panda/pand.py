import pandas as pd

# Pandas module handles many of those edge cases right out of the box and has many parameters that you can change to handle messier CSV files.

# Define the column names as a list
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
         'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
# Read in the CSV file from the webpage using the defined column names
df = pd.read_csv("adult.data", header=None, names=names)

# print(df.head())

# Describe will give you counts and some statistics for continuous variables.
# The only columns describe() function fetched for us are the ones that hold numeric data.

# print(df.describe())

# To see what types of data we have, we can use the info() function:

print(df.info())
