# Matthew Howard
import sys

# Check that exactly 2 arguments are provided: script name and file name
if len(sys.argv) != 3:
    print("Usage: python write.py <filename>,<filename>")

# Get the filename from the command line
f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1,"r") as f1:
    with open(f2,"w") as f2:
        for line in f1:
            f2.write(line.upper())
        