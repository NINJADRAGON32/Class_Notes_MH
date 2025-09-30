#Matthew Howard
def lowerc(text):
    """Lowercase the whol string so we can count the uncapitalized as"""
    return text.lower().count('a')

def main():
    # Take input from user
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")

    """ Count the number of a's in each string """
    count1 = lowerc(string1)
    count2 = lowerc(string2)

    # Compare and print results
    if count1 > count2:
        print("Sentence 1 has more a's than Sentence 2.")
    elif count2 > count1:
        print("Sentence 2 has more a's than Sentence 1.")
    else:
        print("Sentence 1 and Sentence 2 have the same amount of a's.")

main()