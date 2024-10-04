def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

def view_todo_list(todo_list):
    if len(todo_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list):
            status = "Complete" if task['complete'] else "Incomplete"
            print(f"{i+1}. {task['task']} - [{status}]")

def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append({"task": task, "complete": False})
    print(f"Task '{task}' added to the list.")

def remove_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the task number to remove: "))
        removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task['task']}' removed from the list.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_complete(todo_list):
    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the task number to mark complete: "))
        todo_list[task_num - 1]['complete'] = True
        print(f"Task '{todo_list[task_num - 1]['task']}' marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            mark_task_complete(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()