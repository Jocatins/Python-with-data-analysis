# What is an outlier

An outlier is a data point that is distant from other similar points. They may be due to variability in the measurement or may indicate experimental errors. If possible, outliers should be excluded from the data set. However, detecting that anomalous instances might be very difficult, and is not always possible.

-   3 different methods of dealing with outliers:

Univariate method: This method looks for data points with extreme values on one variable.

Multivariate method: Here we look for unusual combinations on all the variables.

Minkowski error: This method reduces the contribution of potential outliers in the training process

# scaling

The scale of your features matter for many machine learning algorithms. Having income values that range from 100 to 100,000 and ages that range from 0 to 100 can cause issues because of the large difference in scale of these two data columns. To deal with this, it is standard to rescale the data. There are many ways to do this, but the two most common ones are:

-   Standard scaling
-   Min/Max scaling.

# Standard scaling

Standard scaling subtracts the mean and divides by the standard deviation. This centers the feature on zero with unit variance.

-   Refer to index.py for Example

# Min/Max scaling

-   Refer to the same example but instead using MinMaxScaler()

# Introduction to categorical data

Sometimes you get categorical data which are variables with a limited and usually fixed number of values.

-   Dealing with categorical data #

# Label encoding

Label encoding works by converting the unique values to a numeric representation. For example, if we have two categories male and female, we can categorize them as numbers:

male as 0
female 1

-   Refer to index2.py

# One-hot encoding

One-hot encoding is similar but creates a new column for each category and fills it with a 1 for each row with that value and zero otherwise.
