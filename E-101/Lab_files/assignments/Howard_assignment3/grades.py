# Matthew Howard
while True:
    grade = int(input("enter the grade pls: "))
    if grade>=0 and grade<=100:
        if grade<70:
            print("Come to office hours")
        elif grade>=70:
            print("passing")

        ui = str(input("would you like to Continue: c/q "))
        if ui == "q":
            break
    else:
        print("invalid grade try again")
