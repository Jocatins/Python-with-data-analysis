# Data visualization tools in Python

In Python, two of the most popular tools for visualizing data are Matplotlib and Seaborn.
These are the tools we will focus on, but there are many others including Bokeh, ggpy, and D3.

-   Matplotlib is sort of the base plotting library in Python. Think of it as a low-level library that allows you to do all sorts of things, but this flexibility can sometimes make it hard to work with. Matplotlib has been around for a while and sometimes can look a bit dated in style.

-   Seaborn was created to help deal with some of these issues. It is built on top of Matplotlib and in its own words, “provides a high-level interface for drawing attractive statistical graphics.

-   Since Seaborn is built on top of Matplotlib, it is pretty easy to mix the two.

# Scatter Plots

Scatter plots are great for plotting two variables to visualize how they might correlate and what relationship there might be between the variables.

Seaborn makes it easy to create scatter plots using the lmplot() function. The key inputs are:

-   x which is the column name for your x-axis variable
-   y which is the column name for your y-axis variable
-   data which is your Pandas dataframe

# Visualization with Bar Plots

Bar plots can be useful when comparing categories. For example, the bar plot below compares the capital gain values across gender.

We can create this bar plot using the barplot() command in Seaborn.

-   The first argument to the command is the column to be used for the groups.
-   The second argument is the column to be used for comparison

<!-- Check index2.py for codes -->

# Visualization with Distributions

A probability distribution is a mathematical function that provides the probabilities of the occurrence of different possible outcomes.

-   Types of distributions

# Histogram

You create a histogram with the distplot() function is Seaborn. You only need to pass one argument which is the continuous variable for which you would like to construct a histogram.

Histograms have a very important parameter - the number of bins. You specify the number of bins with the bin parameter.
If unspecified, Seaborn tries to find a useful number of bins to use. It is important to remember, though that the more bins, the higher variance your plot will have; the fewer bins, the more bias.

<!-- Refer to histo.py -->

# Box plot

A box plot is a graphical view of summary statistics from a distribution.

 <!-- Refer to the img box-plot.png -->

The middle line is the median, the right side of the box is the 75th percentile and the left side the 25th percentile. The whiskers are the lines that stick out from the box. Usually these extend out 1.5 times the interquartile range (IQR) where the IQR is the distance between the 75th and 25th percentiles. Any values outside the whiskers are usually shown as dots, and as we know, could be considered outliers.

-   You can create a box plot using the boxplot function from Seaborn. The only argument you usually have to pass is the first one which is the continuous variable you which to represent with a box plot.

<!-- Refer to box-plot.py for code illustration -->

# Violin Plot

Seaborn has a plot very similar to a box plot called a violin plot. With this plot you have removed the box part of the box plot and replaced it with the kde curve we saw from the distplot() function. This can be valuable as it allows you to see the modality of your distribution.

-   You create a violin plot using the violinplot() function in Seaborn. You just pass it a dataframe and it will create a violin plot for each column in your dataframe.

<!-- Refer to violin-plot.py for code illustration -->

# Joint Plot

Lastly, joint plots can plot the histogram of two variables on one plot and also show the scatter plot in the middle. In the top right, you also get the Pearson correlation coefficient between the variables as well as the p-value.

-   This is done with the jointplot() function from Seaborn.

The first parameter is the variable you would like on the x-axis. The second parameter is the variable you would like on the y-axis

You can also use the kind parameter to change how the scatter points are visualized. I like passing a value of “hex”.

<!-- Refer to violin-joint.py for code illustration -->
