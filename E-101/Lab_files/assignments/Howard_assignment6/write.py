# Matthew Howard
import sys

# Check that exactly 2 arguments are provided: script name and file name
if len(sys.argv) != 2:
    print("Usage: python write.py <filename>")


# Get the filename from the command line
filename = sys.argv[1]

# Open the file for writing and write the words
with open(filename, "w") as file:
    animals = ["cows", "pigs", "dogs", "birds", "cats", "chickens"]
    for animal in animals:
        file.write(animal + "\n")

