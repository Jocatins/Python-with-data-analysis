# Scipy is a Python library for scientific computing

-   A correlation is a numerical measure of the statistical relationship between two variables.
-   For us, those variables will usually be two columns of data, for example, the temperature outside and the likelihood of rain.

-   One way to calculate the correlation between two vectors of data is with Pearson’s r-value.

-   This value ranges between -1 and 1. Where -1 means there is a total negative correlation, 0 means no correlation, and 1 means total positive.

from scipy import stats
import numpy as np

array_1 = np.array([1, 2, 3, 4, 5, 6]) # Create a numpy array from a list
array_2 = array_1 # Create another array with the same values

-   Calculate the correlation which will be 1 since the values are the same

print(stats.pearsonr(array_1, array_2))

Output

(1.0, 0.0)

Since the arrays are the same, we expect there to be a perfectly positive correlation.
The result is a tuple containing two values. The first value is the value of correlation. It’s 1, which means it’s a positive correlation.
Where the second value in the tuple is the p-value.

# Normal distribution

-   The normal distribution is one that is symmetric around the mean and for which values closer to the mean are more common.

Say you needed to generate data from a normal distribution with a mean of 0 and a standard deviation of 10; here is how you would do that:

-   Generate 10 values randomly sampled from a normal distribution with mean 0 and standard deviation of 10

x = stats.norm.rvs(loc=0, scale=10, size=10)

print(x)

Output ---> [ 1.99906974 8.53931197 16.01260419 -15.80071545 -2.27574293
-2.46394475 -3.47593224 -3.55704778 -7.59922317 0.63622101]

The code above uses the loc parameter as the mean, the scale as the standard deviation, and the size as the number of samples to return. If you sampled enough data points and plotted the results, you would see a normal distribution centered around 0 with a standard deviation of 10.

# Probability density function

-   This function will give you the relative likelihood that you would sample a particular value.

from scipy import stats

p1 = stats.norm.pdf(x=-100, loc=0, scale=10) # Get probability of sampling a value of -100
p2 = stats.norm.pdf(x=0, loc=0, scale=10) # Get probability of sampling a value of 0

print(p1)
print(p2)

Output

7.69459862671e-24
0.0398942280401

Above we see that relatively it is much more unlikely to sample the value of -100 (the parameter x) at line 2, from our distribution than a value of 0 (at line 3). This makes sense as our normal distribution is centered on 0 and has a standard deviation of 10.

# Cumulative distribution function

the probability of sampling a value less than or equal to x.

p1 = stats.norm.cdf(x=0, loc=0, scale=10) # Get probability of sampling a value less than or equal to 0

print(p1)

We can see that the cumulative distribution function with x=0 is 0.5 because 0 is the mean and with a normal distribution, half of the data is less than or equal to the mean.

# Calculating descriptive statistics

Lastly, if you have an array of values in Scipy, you can use the describe() function to calculate multiple descriptive statistics for your array. Consider the following program:

print(stats.describe(stats.norm.rvs(loc=0, scale=1, size=500)))

Output ---> DescribeResult(nobs=500, minmax=(-3.252157262991399, 3.000043612506929), mean=-0.015493251234261983, variance=0.986685523908192, skewness=0.08039464724172628, kurtosis=0.21318067918070982)

As you can see above, you get the number of observations, the min, the max, the mean, the variance, the skewness, and the kurtosis of your array.
