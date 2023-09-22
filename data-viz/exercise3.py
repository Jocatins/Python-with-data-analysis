import seaborn as sns            # importing seaborn functionality
import pandas as pd

# Load dataset


def read_csv():
    # Define the column names as a list
    names = ["mpg", "cylinders", "displacement", "horsepower",
             "weight", "acceleration", "model_year", "origin", "car_name"]
    # Read in the CSV file from the webpage using the defined column names
    df = pd.read_csv("auto-mpg.data", header=None,
                     names=names, delim_whitespace=True)
    return df


def line_plot(df):

    # filtering the dataset to obtain the January records for all years
    df = df[df.car_name.str.contains('ford')]

    # plotting a line graph
    sns.lineplot(df.model_year, df.weight)


line_plot(read_csv())

# Before plotting, we need to filter out the data we need. Look at line 20.
# Here we are considering all the rows for which the value in car_name would have ford as a substring

# Line 23 is the most important line. We are using a built-in function lineplot() from seaborn library which takes two main argument:

# column1: Column whose values are to plotted at the x-axis
# column2: Column whose values are to plotted at the y-axis

# At line 26, we are calling the function line_plot(read_csv()).
# First control will transfer to read_csv() at line 7 and we’ll get a dataframe. Then control will go to line 17 and plot will be visualized
