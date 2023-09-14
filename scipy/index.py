from scipy import stats
import scipy

print(scipy.__version__)


# Generate 10 values randomly sampled from a normal distribution with mean 0 and standard deviation of 10
x = stats.norm.rvs(loc=0, scale=10, size=10)

print(x)
