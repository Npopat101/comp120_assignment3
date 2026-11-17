tasks = []

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task "{task}" added successfully!')
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
