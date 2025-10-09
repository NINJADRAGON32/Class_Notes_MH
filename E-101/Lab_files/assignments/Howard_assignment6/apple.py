# Matthew Howard
import sys

# Check that exactly 2 arguments are provided: script name and file name
if len(sys.argv) != 2:
    print("Usage: python write.py <filename>")

# Get the filename from the command line
filename = sys.argv[1]

# Open the file for reading
with open(filename, "r") as f: 
    text = f.read() 

# setting the entire string into the same case
text = text.upper()

count = text.count("APPLE")

print(f"The word apple appears {count} times in {filename}.")