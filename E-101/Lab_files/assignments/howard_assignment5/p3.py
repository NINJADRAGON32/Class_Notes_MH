def myRange(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

# main program
# ask for number of columns
cols = int(input("Enter number of column: "))

# make the list of lists
table = []
for i in range(1, cols + 1):
    table.append(myRange(i))

# print without zeros
print("Without zeros:")
for row in table:
    print(row)

# find the largest row size
max_size = cols

# pad rows with zeros
print("With zeros:")
for row in table:
    while len(row) < max_size:
        row.append(0)
    print(row)
