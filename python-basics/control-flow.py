# The if-else construct

def age_check(age):

    if age > 40:
        print("You are old enough to vote!")
    elif age > 30 and age <= 40:
        print("Between 30 and 40")
    else:
        print("Others")


# print(age_check(45))

# Loops

names = ['tyler', 'karen', 'jill']

for i, name in enumerate(names):
    print("Index: {0}".format(i))

# OR

for x, n in enumerate(names):
    print("Name: {0}".format(x), n)

# loop over the range and only keep the value if greater than 5
numbers_gt_5 = [x for x in range(1, 15) if x > 5]
print(numbers_gt_5)

# We could also increment every value in a list by 1 as below:

nums_plus_one = [x + 1 for x in range(5)]
print(nums_plus_one)

# Built-in functions in Python
# The sort function

my_list = [2, 10, 1, -5, 22]
my_list.sort()  # sorting the list

print(my_list)

my_sorted_list = sorted(my_list, key=abs,  reverse=True)
print(my_sorted_list)

# The Zip Function for:
# Combining two lists into a list of tuples
# The zip actually returns a generator, so we have to wrap it in list() to print it.
# This would not be necessary if you wanted to loop over it though, because generators are iterable:

list_1 = [1, 2, 3]  # create a first list
list_2 = ['x', 'y', 'z']  # create a second list

print(list(zip(list_1, list_2)))  # combine and print

# Breaking a tuple into two lists
# This function can break a tuple into two lists, exactly the reverse of the above use case.

pairs = [('x', 1), ('y', 2), ('z', 3), ("p9")]  # a list of tuples
letters, numbers = zip(*pairs)  # break into two lists

print(letters)  # print the first values of the tuples
print(numbers)  # print the second values of the tuples
