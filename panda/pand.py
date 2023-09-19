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

# print(df.info())

# If a column doesn’t seem to have the correct type, it is easy to convert it to different types using .to_() functions:

# to_numeric()
# to_datetime()
# to_string()

# For example:

#  df['numeric_column'] = pd.to_numeric(df['string_column'])

# You also get the count of non-null values per column and the memory usage of your dataframe from the info command used above.

# Another useful step is to look at unique values for columns.
# Here is an example for the relationship column:

print(df['relationship'].unique())

# [' Not-in-family' ' Husband' ' Wife' ' Own-child' ' Unmarried'
#  ' Other-relative']

# Now we can see all the unique values above and can check the counts of unique values for relationships:

print(df['relationship'].value_counts())

# We can also do these types of counts by specific groups by using the groupby() function.
# This function takes a list of columns by which you would like to group your dataframe.
# It then performs the requested calculations on each group individually and returns the results by group.
# Here is an example:

# print(df.groupby('relationship')['label'].value_counts(normalize=True))

# What we did above was group by the variable, relationship, and then perform value counts on the variable label.
#  For these data, label is whether you make more than 50k. We can see above that 55% of husbands make more than 50k.
# We received percentages because we used the normalize=True parameter.

# You can do many types of calculations on groups using Pandas. For example, here we can see the mean hours worked per week by workclass.

print(df.groupby(['workclass'])['hoursperweek'].mean())

# From the result above, it looks like Federal government workers work more than local workers on average. Never-worked average about 28 hours.


# You can calculate all the pair-wise correlations in your dataframe by using the corr function.

# print(df.corr())


# Convert the string label into a value of 1 when >= 50k and 0 otherwise
# df['label_int'] = df.label.apply(lambda x: ">" in x)
# print(df.corr())

# the describe function of Pandas gives some percentiles, but it is easy to add more:

print(df.describe(percentiles=[.01, .05, .95, .99]))

# A percentile is the value below which a given percent of the data falls.

# We pass the percentile values we want using the percentiles parameter shown above.
