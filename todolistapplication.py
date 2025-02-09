class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display!")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")

    def update_task(self, task_number, new_task):
        try:
            self.tasks[task_number - 1] = new_task
            print(f"Task updated to: {new_task}")
        except IndexError:
            print("Invalid task number! Please try again.")

    def delete_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task}' deleted successfully!")
        except IndexError:
            print("Invalid task number! Please try again.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == 2:
            todo_list.display_tasks()

        elif choice == 3:
            todo_list.display_tasks()
            try:
                task_number = int(input("Enter the task number you want to update: "))
                new_task = input("Enter the new task description: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Invalid input! Please enter a number for the task.")

        elif choice == 4:
            todo_list.display_tasks()
            try:
                task_number = int(input("Enter the task number you want to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input! Please enter a number for the task.")

        elif choice == 5:
            print("Exiting To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
