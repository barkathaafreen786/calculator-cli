import os

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                task, status = line.strip().split("::")
                tasks.append({"task": task, "completed": status == "True"})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}::{task['completed']}\n")

# Show all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found.\n")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✅ Done" if task["completed"] else "❌ Pending"
            print(f"{idx}. {task['task']} [{status}]")
    print()

# Add a new task
def add_task(tasks):
    new_task = input("Enter a new task: ").strip()
    if new_task:
        tasks.append({"task": new_task, "completed": False})
        print("✅ Task added!\n")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"🗑️ Deleted task: {removed['task']}\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("✅ Task marked as completed!\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("=== TO-DO LIST MENU ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            complete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📦 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Enter a number from 1 to 5.\n")

if __name__ == "__main__":
    main()
