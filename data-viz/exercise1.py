# Scatter Plot

import pandas as pd
import seaborn as sns

# Load data


def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower",
             "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("auto-mpg.data", header=None,
                     names=names, delim_whitespace=True)

    return df

# Create the scatter plot


def scatter_plot(df):
    sns.lmplot(x="displacement", y="acceleration", data=df)
    # Remove excess chart lines and ticks for a nicer looking plot
    sns.despine()


# call the function
scatter_plot(read_csv())
