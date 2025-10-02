import math

numbers = []   # list to store rounded numbers

while True:
    value = input("Enter a number (or 'q' to quit): ")
    
    if value == "q":   # stop if user types q
        break
    else:
        # turn input into a float
        num = float(value)
        # round up using math.ceil
        rounded = math.ceil(num)
        # add to list
        numbers.append(rounded)

# print the final list
print("List rounded up:", numbers)