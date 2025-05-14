
def show_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("        TO-DO LIST MANAGER")
    print("="*40)
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Mark task as complete")
    print("4. Delete task")
    print("5. Exit")
    print("-"*40)

def view_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("\nNo tasks found! Your to-do list is empty.")
        return
    
    print("\n" + "="*50)
    print("          YOUR TASKS")
    print("="*50)
    
    for i, task in enumerate(tasks, 1):
        status = "COMPLETED" if task['completed'] else "PENDING"
        print(f"{i}. {task['title']:<30} [{status}]")
    
    print("-"*50)
    print(f"Total tasks: {len(tasks)} | "
          f"Completed: {sum(1 for task in tasks if task['completed'])} | "
          f"Pending: {sum(1 for task in tasks if not task['completed'])}")

def add_task(tasks):
    """Add a new task to the list"""
    while True:
        task_title = input("\nEnter task description (or 'cancel' to go back): ").strip()
        
        if task_title.lower() == 'cancel':
            print("Task creation cancelled.")
            return
        
        if task_title:
            new_task = {
                'title': task_title,
                'completed': False
            }
            tasks.append(new_task)
            print(f"✓ Task '{task_title}' added successfully!")
            return
        else:
            print("Task description cannot be empty. Please try again.")

def complete_task(tasks):
    """Mark a task as completed"""
    if not tasks:
        print("\nNo tasks available to complete!")
        return
    
    view_tasks(tasks)
    
    while True:
        try:
            choice = input("\nEnter task number to mark as complete (or 'cancel'): ").strip()
            
            if choice.lower() == 'cancel':
                print("Operation cancelled.")
                return
            
            task_num = int(choice) - 1
            
            if 0 <= task_num < len(tasks):
                if tasks[task_num]['completed']:
                    print(f"Task '{tasks[task_num]['title']}' is already completed!")
                else:
                    tasks[task_num]['completed'] = True
                    print(f"✓ Task '{tasks[task_num]['title']}' marked as complete!")
                return
            else:
                print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list"""
    if not tasks:
        print("\nNo tasks available to delete!")
        return
    
    view_tasks(tasks)
    
    while True:
        try:
            choice = input("\nEnter task number to delete (or 'cancel'): ").strip()
            
            if choice.lower() == 'cancel':
                print("Operation cancelled.")
                return
            
            task_num = int(choice) - 1
            
            if 0 <= task_num < len(tasks):
                confirm = input(f"Are you sure you want to delete '{tasks[task_num]['title']}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    deleted_task = tasks.pop(task_num)
                    print(f"✓ Task '{deleted_task['title']}' deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return
            else:
                print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
        
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main application loop"""
    # Initialize empty task list
    tasks = []
    
    print("Welcome to the Simple To-Do List CLI!")
    print("Let's get organized!")
    
    # Main application loop
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                view_tasks(tasks)
            
            elif choice == '2':
                add_task(tasks)
            
            elif choice == '3':
                complete_task(tasks)
            
            elif choice == '4':
                delete_task(tasks)
            
            elif choice == '5':
                print("\nThank you for using the To-Do List Manager!")
                print("Stay organized and have a great day!")
                break
            
            else:
                print("\nInvalid choice! Please select a number between 1 and 5.")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for using the To-Do List Manager!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")

# Run the application
if __name__ == "__main__":
    main()