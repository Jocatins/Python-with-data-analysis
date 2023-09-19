# Pivot Table
# we can pivot our data using pandas pivot_table functionality. To do so, we will use the pivot_table() function.

import numpy as np
import pandas as pd
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
         'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']
train_df = pd.read_csv("adult.data", header=None, names=names)

# Pivot the data frame to show by relationship, workclass (rows) and label (columns) the average hours per week.
print(pd.pivot_table(train_df, values='hoursperweek', index=['relationship', 'workclass'],
                     columns=['label'], aggfunc=np.mean).round(2))

# The values parameter is the column being used for aggregation,
# the index parameter is for the index values that creates multiple rows,
#  and the columns parameter is for the value on which you want to have multiple columns created.

# Cross Tab

# Crosstab is a nice way to get frequency tables.
# What you do is pass two columns to the function and you will get the frequency of all the pair-wise combinations of those two variables.

print(pd.crosstab(train_df['label'], train_df.relationship))

#  We can also normalize the results using the normalize=True parameter.

print(pd.crosstab(train_df['label'], train_df.relationship, normalize=True))
