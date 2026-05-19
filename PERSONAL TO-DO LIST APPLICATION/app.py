def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

            if not tasks:
                print("\nNo tasks found.\n")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")

    except FileNotFoundError:
        print("\nNo task file found.\n")


def add_task():
    task = input("Enter new task: ")

    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task added successfully!\n")


def remove_task():
    show_tasks()

    try:
        task_number = int(input("\nEnter task number to remove: "))

        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print(f"Removed task: {removed}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")