# Matthew Howard
while True:
    emp_type = input("Enter an employee type (a/i/e): ").lower()
    
    if emp_type == "a":
        yearly_income = 7500 * 10
        print(f"Academic Yearly Income is ${yearly_income:,}")
        break
    elif emp_type == "i":
        yearly_income = 6000 * 12
        print(f"Information Technologist Yearly Income is ${yearly_income:,}")
        break
    elif emp_type == "e":
        yearly_income = 9000 * 12
        print(f"Engineer Yearly Income is ${yearly_income:,}")
        break
    else:
        print("Unknown Employee Type! Enter again.")