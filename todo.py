# Simple Console-Based To-Do List in Python

# List to store tasks
tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("\n📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("✅ Task added!")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Task '{removed}' deleted.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
