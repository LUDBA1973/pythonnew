students = {}

def add_student(name, grade):

    try:
        grade = int(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        if not name.strip():
             raise ValueError("Student name cannot be empty.")
        if not name.replace(" ", "").isalpha():  
             raise ValueError("Student name must contain only alphabets.")
    except ValueError as x:
        print(f"Error: {x}")

    else:
        students[name] = grade
        print(f"Added {name} with grade {grade}.")

def update_grade(name, grade):

    try:
        if name not in students:
            raise KeyError(f"Student '{name}' not found.")
        grade = int(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")    
    except KeyError as z:
        print(f"Error: {z}")
    except ValueError as x:
        print(f"Error: {x}")
    else:
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}.")

def display_students():
    if students=={}:
        print("No students in the system.")
    else:
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"Name:{name} Grade: {grade}")



while True:
        print("\nChoose an operation: 1-add, 2-update, 3-display, 4-exit")
        operation = input("Enter operation(1/2/3/4): ").strip().lower()
        
        if operation == "1":
            name = input("Enter student name: ")
            grade = input("Enter grade (0-100): ")
            add_student(name, grade)
        elif operation == "2":
            name = input("Enter student name: ")
            grade = input("Enter new grade (0-100): ")
            update_grade(name, grade)
        elif operation == "3":
            display_students()
        elif operation == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid operation. Please choose again.")
