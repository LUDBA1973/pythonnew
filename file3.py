TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from the todo.txt file."""
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the todo.txt file."""
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(f"[ ] {task}")
    save_tasks(tasks)
    print("Task added successfully.")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")

def mark_completed(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[X]")
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    """Delete a task from the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                mark_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
