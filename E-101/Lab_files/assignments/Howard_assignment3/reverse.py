#Matthew Howard
sentence = input("Enter a sentence: ")

sentence_no_spaces = sentence.replace(" ", "")

length = len(sentence_no_spaces)
print("Length of sentence without spaces:", length)

print("Reversed sentence (without spaces):")
for i in range(length - 1, -1, -1):  
    print(sentence_no_spaces[i])