# Matthew Howard
def salesperson_salary():
    """Calculate yearly salary for a salesperson before tax."""
    monthly_salary = float(input("Please enter the monthly salary: "))
    products_sold = int(input("Please enter the number of products sold: "))
    yearly_salary = (monthly_salary * 12) + (products_sold * 100)
    return yearly_salary

def office_worker_salary():
    """Calculate yearly salary for an office worker before tax."""
    monthly_salary = float(input("Please enter the monthly salary: "))
    overtime_hours = int(input("Please enter the number of overtime hours worked: "))
    yearly_salary = (monthly_salary * 12) + (overtime_hours * 20)
    return yearly_salary

def part_time_salary():
    """Calculate yearly salary for a part-time employee before tax."""
    monthly_salary = float(input("Please enter the monthly salary: "))
    months_worked = int(input("Please enter the number of months worked: "))
    yearly_salary = monthly_salary * months_worked
    return yearly_salary

def after_tax(salary):
    """Calculate income after tax."""
    if salary < 30000:
        return salary * 0.90  # 10% tax
    else:
        return salary * 0.75  # 25% tax

def main():
    employee_type = input("Please enter the employee type (S, O, P): ").strip().upper()

    if employee_type == "S":
        gross_salary = salesperson_salary()
    elif employee_type == "O":
        gross_salary = office_worker_salary()
    elif employee_type == "P":
        gross_salary = part_time_salary()
    else:
        # edge cases
        print("Error: Must enter employee type")
        return

    net_salary = after_tax(gross_salary)
    print(f"Output: This employee makes ${gross_salary:.0f} before tax and ${net_salary:.0f} after tax.")

main()