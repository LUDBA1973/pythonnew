

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    
    try:
        marks = float(marks)
    except ValueError:
        print("Invalid marks. Please enter a numeric value.")
        return
    
    with open("grades.txt", "a") as file:
        file.write(f"{roll_no},{name},{marks}\n")
    print("Student record added successfully!")

def calculate_average():
    try:
        with open("grades.txt", "r") as file:
            records = [line.strip().split(',') for line in file]
            marks = [float(record[2]) for record in records]
            avg_marks = sum(marks) / len(marks)
            print(f"Average Marks: {avg_marks:.2f}")
    except FileNotFoundError:
        print("No student data available.")
    except ZeroDivisionError:
        print("No records found to calculate average.")

def find_highest_lowest():
    try:
        with open("grades.txt", "r") as file:
            records = [line.strip().split(',') for line in file]
            marks = [(record[1], float(record[2])) for record in records]
            
            highest = max(marks, key=lambda x: x[1])
            lowest = min(marks, key=lambda x: x[1])
            
            print(f"Highest Scorer: {highest[0]} - {highest[1]}")
            print(f"Lowest Scorer: {lowest[0]} - {lowest[1]}")
    except FileNotFoundError:
        print("No student data available.")
    except ValueError:
        print("Error processing file data.")

def generate_pass_fail_list():
    try:
        with open("grades.txt", "r") as file:
            records = [line.strip().split(',') for line in file]
            passed = [record[1] for record in records if float(record[2]) >= 40]
            failed = [record[1] for record in records if float(record[2]) < 40]
            
            print("Passed Students:", ", ".join(passed) if passed else "None")
            print("Failed Students:", ", ".join(failed) if failed else "None")
    except FileNotFoundError:
        print("No student data available.")
    except ValueError:
        print("Error processing file data.")


while True:
        print("\nStudent Grade Processing System")
        print("1. Add Student Record")
        print("2. Calculate Average Marks")
        print("3. Find Highest & Lowest Scorer")
        print("4. Generate Pass/Fail List")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            calculate_average()
        elif choice == '3':
            find_highest_lowest()
        elif choice == '4':
            generate_pass_fail_list()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


