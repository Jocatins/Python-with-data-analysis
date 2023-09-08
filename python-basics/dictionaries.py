# Dictionaries in Python

# They are initialized with {}

# Initialize the dictionary.
# Keys are first then a : then the value
my_dict = {"age": 22, "birth_year": 1999,
           "name": "jack", "siblings": ["jill", "jen"]}

# Get the value for the key age
print("---0---")
print(my_dict['age'])

# Check if age is a key
print("---1---")
print('age' in my_dict)

# Check if company is a key
print("---2---")
print('company' in my_dict)

# Get the value for the key age
print("---3---")
print(my_dict.get('age'))

# Get the value for they key company
# If it doesn't exist, return 1
print("---4---")
print(my_dict.get('company', 1))

# Return all the keys
print("---5---")
print(my_dict.keys())

# Return all the values
print("---6---")
print(my_dict.values())

# Return all the key, value pairs
print("---7---")
print(my_dict.items())
