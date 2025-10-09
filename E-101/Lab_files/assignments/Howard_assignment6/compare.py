# Matthew Howard
import sys

# Check that exactly 2 arguments are provided: script name and file name
if len(sys.argv) != 3:
    print("Usage: python write.py <filename>,<filename>")

# Get the filename from the command line
f1 = sys.argv[1]
f2 = sys.argv[2] 

def count_characters(filename): 
    with open(filename, "r") as f: 
        text = f.read() 
        # Remove spaces and newlines 
        cleaned = text.replace(" ", "").replace("\n", "") 
        return len(cleaned)

# Count characters in each file 
count1 = count_characters(f1) 
count2 = count_characters(f2) 

if count1 > count2: 
    print(f"{f1} has more characters than {f2}") 
elif count2 > count1: 
    print(f"{f2} has more characters than {f1}") 
else: 
    print(f"{f1} and {f2} have the same number of characters")