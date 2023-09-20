from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')

# Load data
boston_data = load_boston()
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Create the histogram plot
sns.distplot(boston_df.NOX, kde=False)

# kde=False. With this equal to True, it plots the shape of the distribution.

# With 100 bins
# sns.distplot(boston_df.NOX, bins=100, kde=False)

# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()
