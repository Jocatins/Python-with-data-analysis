import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights_long = sns.load_dataset("flights")
# Pivot the dataset from long to wide format
flights = flights_long.pivot("month", "year", "passengers")
# Create a larger figure size to plot on
f, ax = plt.subplots(figsize=(12, 6))
# Create the heat map
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax, cmap='Blues')

# Above, we plotted the number of airline passengers by month and year.
# In our code, we used Matplotlib to adjust the figure size to make it larger, (12,6).
# That returns a value we called “ax” and we pass this to Seaborn with the ax parameter.
# We also use the annot=True parameter to add the actual values to our cells.

# The other option that we call out is the cmap parameter. This allowed us to adjust the color used for the cells by passing “Blues”.

# We can see over the years the number of passengers has increased, and that July and August are consistently the most popular months.
