student_grades = {}

def add_student(name, grade):
    try:
        # Check if name is not a string (which is unlikely because input() returns strings)
        if not isinstance(name, str):
            raise Exception("Student name must be a string.")

      

       
        if not grade.replace('.', '', 1).isdigit():  
            raise ValueError("Grade must be a number.")

        grade = float(grade)  # Convert to float

        if 0 <= grade <= 100:  # Check grade range
            student_grades[name] = grade  # Store in dictionary
            print("Success: Student added.")
        else:
            print("Error: Grade must be between 0 and 100.")
    except ValueError as ve:
        print(f"Error: Invalid grade. {ve}")
    except Exception as ee:
        print(f"Error: {ee}")



def update_grade(name, grade):

    try:
        if name not in student_grades:
            raise KeyError(f"Student '{name}' not found.")
        grade = float(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        else:
            student_grades[name] = grade
            print(f"Updated {name}'s grade to {grade}.")
    except KeyError as ke:
        print(f"Error: {ke}")
    except ValueError as ve:
        print(f"Error: {ve}")

def display_students():
    if not student_grades:
        print("No students in the system.")
    else:
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"Name:{name} Grade: {grade}")

def main():

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


main()
