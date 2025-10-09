# Matthew Howard
import sys

# Check that exactly 2 arguments are provided: script name and file name
if len(sys.argv) != 2:
    print("Usage: python write.py <filename>")

# Get the filename from the command line
filename = sys.argv[1]
 
# Open the file for reading and print the farm sentences 
with open(filename, "r") as file:
    for line in file: 
        animal = line.strip() 
        print(f"The farm has {animal}")