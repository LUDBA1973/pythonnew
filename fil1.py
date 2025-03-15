import os

EMPLOYEE_FILE = "employees.txt"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    
    with open(EMPLOYEE_FILE, "a") as file:
        file.write(f"{emp_id},{name},{department}\n")
    print("Employee added successfully!\n")

def view_employees():
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.\n")
        return
    
    with open(EMPLOYEE_FILE, "r") as file:
        employees = file.readlines()
    
    if not employees:
        print("No employee records found.\n")
    else:
        print("Employee Records:")
        for emp in employees:
            emp_id, name, department = emp.strip().split(",")
            print(f"ID: {emp_id}, Name: {name}, Department: {department}")
    print()

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.\n")
        return
    
    with open(EMPLOYEE_FILE, "r") as file:
        for emp in file:
            emp_data = emp.strip().split(",")
            if emp_data[0] == emp_id:
                print(f"Employee Found - ID: {emp_data[0]}, Name: {emp_data[1]}, Department: {emp_data[2]}\n")
                found = True
                break
    
    if not found:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if not os.path.exists(EMPLOYEE_FILE):
        print("No employee records found.\n")
        return
    
    with open(EMPLOYEE_FILE, "r") as file:
        employees = file.readlines()
    
    with open(EMPLOYEE_FILE, "w") as file:
        deleted = False
        for emp in employees:
            emp_data = emp.strip().split(",")
            if emp_data[0] != emp_id:
                file.write(emp)
            else:
                deleted = True
        
    if deleted:
        print("Employee deleted successfully!\n")
    else:
        print("Employee not found.\n")


while True:
        print("\nEmployee Record Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


