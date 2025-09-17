#Matthew Howard
string1 = str(input("enter your string pls: "))
length = int(len(string1))
#if the string has an odd number of length this will make sure the first substring has the smaller length
if length%2==1:
    length=length-1
#split the string in half
sub1 = string1[0:int(length/2)]
sub2 = string1[int(length/2):]
#reverse the order
reverse = sub2+sub1
print(reverse)
