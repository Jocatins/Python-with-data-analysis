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


def bar_plot(df):
    df = df[df.car_name.str.contains('ford')]
    df = df[df["model_year"].isin([75])]

    # Create the bar plot
    sns.barplot(df['car_name'], df['cylinders'])
    # Remove excess chart lines and ticks for a nicer looking plot
    sns.despine()


bar_plot(read_csv())

# To plot a visualization, we import seaborn module at line 2.

# Moving towards the main implementation, look at the header of the bar_plot(df) function at line 17. It takes one arguments as input:

# df: A dataframe containing the dataset in the form of a matrix.

#  Before plotting, we need to filter out the data we need. Look at line 18.

#  Here we are considering all the rows for which the value in car_name would have ford as a substring
# Next, we are keeping all the rows for which model_year is 1975

# Line 22 is the most important line. We are using a built-in function barplot from seaborn library which takes two main argument:

# column1: Column whose values are to plotted at the x-axis
# column2: Column whose values are to plotted at the y-axis

# We set car_name as x and cylinders as y according to the problem statement

# At line 22, we are just trying to make the plot look clean using function despine().

#  At line 27, we are calling the function bar_plot(read_csv())
