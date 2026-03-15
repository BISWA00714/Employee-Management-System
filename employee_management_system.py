# Step:1 - Create a Dictionary of Employee to store employee information with attributes like emp_id, name, age, and department salary.
Employees = {
    "101": {"name": "Biswajit", "age": 24, "department": "HR", "salary": 50000},
    "102": {"name": "Madhu", "age": 28, "department": "IT", "salary": 60000},
    "103": {"name": "Swayam", "age": 6, "department": "Finance", "salary": 70000},
    "104": {"name": "Satntanu", "age": 30, "department": ".net_developer", "salary": 55000},
    "105": {"name": "Kanhu", "age": 50, "department": "Marketing", "salary": 65000},
    "106": {"name": "Bimala", "age": 40, "department": "Data Analyst", "salary": 75000},
    "107": {"name": "Krishna", "age": 40, "department": "Data Scientist", "salary": 155000},
}   


# Step:2 - Create a function to add a new employee to the dictionary.
def add_employee():
    emp_id=input("Enter Employee ID: ")
    if emp_id in Employees:
        print("Employee ID already exists. Please try again.")
        return
    name=input("Enter Employee Name: ")
    age=int(input("Enter Employee Age: "))
    department=input("Enter Employee Department: ")
    salary=float(input("Enter Employee Salary: "))

    Employees[emp_id] = {"name": name, "age": age, "department": department, "salary": salary}

    print(f"Employee {name} added successfully.")

# Step:3 - Create a function to view all employees in the dictionary.
def view_employees():

    if not Employees:
        print("No employees available.")
        return
    
    print("\nEmployee Records :")
    print("-" * 60) 
    print(f"{'ID':<10} {'Name':<20} {'Age':<10} {'Department':<15} {'Salary':<10}")
    print("-" * 60)

    for emp_id, data in Employees.items():
        print(f"{emp_id:<10} {data['name']:<15} {data['age']:<10} {data['department']:<15} {data['salary']:<10}")

# Step:4 - Create a function to update an existing employee's information in the dictionary.
def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in Employees:
        emp = Employees[emp_id]

        print("\nEmployee Found:")
        print(f"Employee ID: {emp_id}")
        print(f"Name: {emp['name']}")
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']}")
    else:
        print("Employee not found.")

def main_menu():

    while True:
        print("\n======Employee Management System=====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()