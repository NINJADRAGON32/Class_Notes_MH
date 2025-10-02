import random as r
fruits=['apple','banana','blueberries','orange','watermelon']
with open('fruits.txt','w') as f:
    for i in range (100):
        f.write(fruits[r.randrange(0,5)]+'\n')


        
