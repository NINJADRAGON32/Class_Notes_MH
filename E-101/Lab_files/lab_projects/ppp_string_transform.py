ui = str(input("enter your string: "))
change = int(input("which change would you like: "))
if change ==1:
    ui = ui.upper()
    print(ui)
elif change ==2:
    ui = ui.lower()
    print(ui)
elif change ==3:
    ui =ui.replace(" ","_")
    print(ui)
elif change ==4:
    count = ui.lower()
    print(f"there are {count.count("a")} instances of the letter a") 


