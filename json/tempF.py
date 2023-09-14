import tempfile

tmp = tempfile.NamedTemporaryFile()

# Open the file for writing. And write the data.

with open(tmp.name, 'w') as f:
    f.write("James|22|M\n")
    f.write("Sarah|31|F\n")
    f.write("Mindy|25|F")


# Read in the data from our file, line by line
with open(tmp.name, "r") as f:
    for line in f:
        print(line)

# We use the open() command to read the file. We first pass the name of the file we want to process and then an r which stands for read.
# Since we used the with as functionality in Python, our filehandle is now represented as the variable f and is only relevant within this scope.
# This is good practice for reading files because you don’t have to worry about closing the filehandle.
# Once you have a filehandle, Python makes it very easy to access the lines. The variable f is now an iterable where each iterable is a line of the file.
#  Thus, when we d0

# for line in f

# We are just looping over the lines of our file.
# The code above only prints out those lines, but since we have direct access to the lines of our file, we can do whatever we want in our processing.
# For example, here is code that takes only the first value of each row and appends them to a list.


tmp = tempfile.NamedTemporaryFile()

# Open the file for writing and write our data
with open(tmp.name, 'w') as f:
    f.write("James|22|M\n")
    f.write("Sarah|31|F\n")
    f.write("Mindy|25|F")

first_values = []  # Define a list to store the first values of each row
with open(tmp.name, "r") as f:  # Open the file to read
    for line in f:  # Loop over each line
        # Split each line by the | character into a list
        row_values = line.split("|")
        first_values.append(row_values[0])  # Add the first value to our list

print(first_values)
