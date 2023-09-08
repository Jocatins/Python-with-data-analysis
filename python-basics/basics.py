# Coding Preambles
#  Importing Functionalities

from collections import Counter

marriage_ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 25]  # create a list
value_counts = Counter(marriage_ages)  # apply the counter functionality
print(value_counts.most_common())

# The value with the most occurrence appears first.

# [(25, 3), (22, 2), (24, 2), (30, 1), (26, 1), (35, 1)]

# Functions


def add_two_values(x, y):  # function header
    z = x + y
    return z


print(add_two_values(100, 5))

# Functions can also be anonymous, meaning that you don’t have to declare them with the above structure.
# Instead, you can use the lambda keyword.


def add_two_numbers(x, y):

    z = x + y
    return z  # function return


result = add_two_numbers(100, 5)
print("Fero's pattern: ", result)


# Lambda

def y(x, y): return x + y


print("lambda-function:", y(120, 10))
