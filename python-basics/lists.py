# Lists in PY
# Slices

# When slicing, the first number is included in the return set while the last number is not. For example:
p1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p2 = p1[1:5]

print(p2)


# This creates the list
depths = [1, 5, 3, 6, 4, 7, 10, 12]

# This outputs the first 5 elements. No number before the : implies 0
first_5_depths = depths[:5]

print("---0---")
print("first 5 depths:", first_5_depths)

# You can easily sum
print("---1---")
print("sum of depths:", sum(depths))

# And take the max
print("---2---")
print("max of depths:", max(depths))

# Slicing with a negative starts from the end, so this returns the last element
print("---3---")
print(depths[-1])

# This returns the end of the list starting from the second to the end
# Nothing after the : implies the end of the list
print("---4---")
print(depths[-2:])

# This returns the second, third, and forth elements
# Remember counting starts at zero!
print("---5---")
print(depths[2:5])

# These commands check if a value is contained in the list
print("---6---")
print(22 in depths)
print(1 in depths)

# This is how you add another value to the end of your list
depths.append(44)
print("---7---")
print(depths)

# You can extend a list with another list
depths.extend([100, 200])
print("---8---")
print(depths)

# You can also modify a value
# This replaces the 4th value with 100
depths[4] = 100
print("---9---")
print(depths)

# Or you can do insert to accomplish the same thing
depths.insert(5, 1000)
print("---10---")
print(depths)

# Generators

# Generators are objects you can loop over like a list, but they are lazy. It means they don’t have to store the entire list in memory
# Instead they return the next value in the list only when asked, making them very memory efficient.
# Because of this property, you can have a function that generates an infinite list;
# it never stores the value in memory but just keeps track of the last value returned and returns that value + 1 when asked for another value.
