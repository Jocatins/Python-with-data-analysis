# Sets in Python #

# Sets are another useful data type.
# Sets are an unordered collection of unique elements, which means any duplicates are automatically removed.
# Sets allow you to do operations like union, intersection, and difference.

my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(1)
# Note that the set only contains a single 1 value
print("---0---")
print(my_set)

my_set2 = set()
my_set2.add(1)
my_set2.add(2)
my_set2.add(3)
my_set2.add(4)
print("---1---")
print(my_set2)

# Prints the overlap
print("---1---")
print(my_set.intersection(my_set2))
print("---2---")

# Prints the combination
print(my_set.union(my_set2))

# Prints the difference (those in my_set but not my_set2)
print("---3---")
print(my_set.difference(my_set2))
