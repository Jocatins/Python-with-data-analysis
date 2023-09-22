from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

# Load data as explained in introductory lesson
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Only keep for ages 96 and 98.2
boston_df = boston_df[boston_df["AGE"].isin([96, 98.2])]

# Create the bar plot
sns.barplot(boston_df['AGE'], boston_df['NOX'])
# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()

# In the code, we limit our data to only include homes with age of 96 or 98.2 to simplify our example.

# The first argument to the barplot() command is the AGE column and the second argument is the NOX column.
# Thus, the plot shows the average NOX value by AGE.

# Seaborn also plots the error bars (the black lines).
# The error bars are calculated via bootstrapping which randomly resamples our data with replacement.
# It then draws 95% error bars which are the 95th and 5th percentiles.
