student_grades = {}


def add_student(name, grade):    
    grade = float(grade)
    if name.strip():
        if grade > 0 and grade < 100:
           student_grades[name] = grade
           print(f"Added {name} with grade {grade}.") 
       
        elif not name.strip():
          print("Student name cannot be empty.")

        elif name.strip() :
          if grade < 0 or grade > 100:
            print("grade must be in 0-100")
           
 

def update_grade(name, grade):

        if name not in student_grades:
            print(f"Student '{name}' not found.")
        grade = float(grade)
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")

def display_students():
    if not student_grades:
        print("No students in the system.")
    else:
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"Name:{name} Grade: {grade}")

def main():

    while True:
        print("\nChoose an operation: add, update, display, exit")
        operation = input("Enter operation: ").strip().lower()
        
        if operation == "add":
            name = input("Enter student name: ")
            grade = input("Enter grade (0-100): ")
            add_student(name, grade)
        elif operation == "update":
            name = input("Enter student name: ")
            grade = input("Enter new grade (0-100): ")
            update_grade(name, grade)
        elif operation == "display":
            display_students()
        elif operation == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid operation. Please choose again.")


main()
