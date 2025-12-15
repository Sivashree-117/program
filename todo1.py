def show_menu():
    print("\n---- TO-DO LIST MENU ----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    tasks = load_tasks()

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task + "\n")
        save_tasks(tasks)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print("Deleted:", removed.strip())
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
