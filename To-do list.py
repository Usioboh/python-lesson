
task = []


def add():
    x = input("Enter your task\n")
    task.append(x)
    print("Task added!")


def view():
    if not task:
        print("No task has been added")
    else:
        print("Your tasks:")
        for t in task:
            print(t)


def main():
    while True:
        print("To-Do List")
        print("1. Add a task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Pick a number.....\n")
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            print("Goodbye👋")
        else:
            print("invalid choice")


main()
