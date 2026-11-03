
name = input("Enter Employee Name: ")
print(f"Data type: {type(name)}")


emp_id = int(input("Enter Employee ID: "))
print(f"Data type: {type(emp_id)}")


salary = float(input("Enter Salary: "))
print(f"Data type: {type(salary)}")


department = input("Enter Department: ")
print(f"Data type: {type(department)}")


active_input = input("Is the employee active? (yes/no): ")
active = active_input.strip().lower() == 'yes'
print(f"Data type: {type(active)}")


print("\n--- Employee Details ---")
print(f"{'Name':<12}: {name}")
print(f"{'ID':<12}: {emp_id}")
print(f"{'Salary':<12}: {salary}")
print(f"{'Department':<12}: {department}")
print(f"{'Active':<12}: {active}")