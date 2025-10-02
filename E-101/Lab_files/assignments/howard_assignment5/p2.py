# gradebook_simple.py

# empty list for students
gradebook = []

# ask how many students
num_students = int(input("Enter Number of Students: "))

# loop to collect names and grades
for i in range(num_students):
    name = input("Enter Student #" + str(i + 1) + " Name: ")
    grade = int(input("Enter Student #" + str(i + 1) + " Grade: "))
    
    # student format: [id, name, grade]
    student = [i + 1, name, grade]
    
    # add to gradebook
    gradebook.append(student)

# --- Manual Sorting by Grade --
# Make a copy so we don’t mess up the original list
sorted_students = gradebook[:]

n = len(sorted_students)
for a in range(n):
    for b in range(0, n - a - 1):
        if sorted_students[b][2] < sorted_students[b + 1][2]:
            # swap if grade is smaller
            temp = sorted_students[b]
            sorted_students[b] = sorted_students[b + 1]
            sorted_students[b + 1] = temp

# ---- Print the top 3 students ---
if len(sorted_students) >= 1:
    print("First Place is", sorted_students[0][1])
if len(sorted_students) >= 2:
    print("Second Place is", sorted_students[1][1])
if len(sorted_students) >= 3:
    print("Third Place is", sorted_students[2][1])

# --- Print the entire class list ---
print(gradebook)
