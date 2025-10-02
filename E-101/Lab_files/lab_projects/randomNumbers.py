import random 
f = open ('random_numbers.txt','w')
for i in range(1000):
    number = random.randrange(0,10)
    f.write(str(number)+"\n")
f.close()

histogram =[0] *10
f = open('random_numbers.txt','r')
for line in f:
    number = int(line.strip())
    histogram[number] += 1
f.close()
for i in range (10):
    print(str(i)+':'+'*'*histogram[i])
