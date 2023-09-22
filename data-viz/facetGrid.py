import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
flights = sns.load_dataset("flights")
# Subset the data to years >= 1956 to more easily fit on the plot
flights = flights[flights.year >= 1956]

g = sns.FacetGrid(flights, row="year", margin_titles=True)
g.map(plt.plot, "passengers", color="steelblue")

# First, we created a FacetGrid by passing our dataframe, which in this example is called flights.
# We then pass the row variable (year) we want to use in the resulting plot.
# You can see in our plot above that we have one plot per year. Margin titles tell the plots to add the titles in the margin.

# Once we have our FacetGrid, we call the map function in order to map data onto our grid.

#  First, we tell it what type of plot we want to use. In this example, we use a line plot from Matplotlib.
# We then pass the variable we want plotted, passengers.
