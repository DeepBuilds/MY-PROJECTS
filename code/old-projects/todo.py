import os

TODO_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: {task}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index - 1 < len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Removed: {removed}")
    else:
        print("❗ Invalid task number.")

def menu():
    while True:
        print("\n--- TO-DO APP ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            list_tasks()
        elif choice == "2":
            task = input("Enter task: ").strip()
            add_task(task)
        elif choice == "3":
            list_tasks()
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(num)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
