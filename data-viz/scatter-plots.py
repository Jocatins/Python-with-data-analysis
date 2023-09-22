from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the palette and style to be more minimal
sns.set(style='ticks', palette='Set2')
# Load the boston dataset from sklearn.datasets
boston_data = load_boston()
# Enter the boston data into a dataframe
boston_df = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)

# Print the first 5 rows to confirm ran correctly
# print(boston_df.head())

# Create the scatter plot
sns.lmplot(x="CRIM", y="NOX", data=boston_df)

# Remove excess chart lines and ticks for a nicer looking plot
sns.despine()


# Note-- load_boston was not found in the latest version of scikit learn, so I did an installation of pip install scikit-learn==1.1.3
