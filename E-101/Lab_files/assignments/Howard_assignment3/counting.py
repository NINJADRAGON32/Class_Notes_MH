# Matthew Howard
n = int(input("Enter a number: "))
one =""
for i in range(n, 0, -1):
    for j in range(i):
        one += "1 " 
    print(f"{i}: {one}")
    one =""
    
