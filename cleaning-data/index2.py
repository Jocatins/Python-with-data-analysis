import pandas as pd

# Create series with male and female values
non_categorical_series = pd.Series(
    ['male', 'female', 'male', 'female'])
# Convert the text series to a categorical series
categorical_series = non_categorical_series.astype('category')
# Print the numeric codes for each value
print(categorical_series.cat.codes)
# Print the category names
print(categorical_series.cat.categories)

# We cast the column using the astype() function and pass the type of category
# This finds all the unique values in our column and assigns each a unique integer value while still maintaining the string values

# You can get the integer values by adding .cat.codes to the end of your category series.

# You get the string values by adding .cat.categories to the end of your category series.

print("----- One-hot Category--------")

print(pd.get_dummies(non_categorical_series))

# We see that we just had to use the get_dummies() call on our series and it automatically makes new columns for each unique
# value in our series and fills them with a 1 or 0 as appropriate.
