# Jeffrey Martin
# 3/29/2026
# P3HW2_Salary_MartinJeffrey.py
# Salary Calculator

# request employee info
name = input("Enter employee's name: ")
hours_worked = float(input("Enter hours worked: "))
rate = float(input("Enter pay rate: "))

# Evaluate overtime
if hours_worked > 40:
    # Calculate overtime
    overtime_hours = hours_worked - 40
    # Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular hours
    regular_pay = 40 * rate
    # Calculate Gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours_worked * rate
    gross_pay = regular_pay


# Display results
print("------------------------------------------------")
print(f'Employee Name: {name}')
print(f'{"Hours Worked":15}{"Pay Rate":12}{"Overtime Pay":12}{"Regular Pay":15}{"Gross Pay":12}')
print("----------------------------------------------------------------------------------------------")
print(f'{hours_worked:<15}{rate:<12}{overtime_pay:<12}{regular_pay:<15}{gross_pay:<12}')
