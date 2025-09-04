weight =float(input("Enter your weight in kg"))

height = float(input("enter your height in cm"))

#convert height to meters
height = height/100

ans = weight/(height*height)

print(f'your bmi is {ans:.2f}')