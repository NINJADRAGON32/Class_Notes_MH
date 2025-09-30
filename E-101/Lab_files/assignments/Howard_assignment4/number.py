# Matthew Howard
def check_even_odd(n):
    """Check if a number is even or odd and print the result."""
    if n % 2 == 0:
        print(f"{n} is even!")
    else:
        print(f"{n} is odd!")

def main():
    """ This function just grabs the users input"""
    numbers = []
    print("Enter 5 integers:")

    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    print("\nResults:")
    for n in numbers:
        check_even_odd(n)

main()