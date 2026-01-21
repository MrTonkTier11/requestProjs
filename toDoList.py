# token: <FirstName-LastName-Last4ID>
# just edit line 1, ganyan daw kasi sabi lagay ng personal token. 
def show_tasks(tasks):
    #Displays current tasks with status, title, and bulleted description.
    if not tasks:
        print("\nYour list is empty!")
        return

    print("\n" + "=" * 30)
    print("       YOUR TO-DO LIST")
    print("=" * 30)
    
    done_count = 0
    for i, task in enumerate(tasks):
        #for displaying of title and desc of the task
        title = task[0]
        is_done = task[1]
        description = task[2]
        
        status = "✔ [DONE]" if is_done else "☐ [PENDING]"
        if is_done:
            done_count += 1
            
        # Print Title Line
        print(f"{i + 1}. {status} {title}")
        # Print Bulleted Description (Indented)
        print(f"   • Description: {description}")
        print("-" * 30)
    
    total = len(tasks)
    pending = total - done_count
    print(f"Summary: {pending} Pending, {done_count} Done (Total: {total})")
    print("=" * 30)

def get_valid_index(tasks, prompt):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(tasks):
                return index
        print(f"Invalid input. Please enter a number between 1 and {len(tasks)}.")

def main():
    
    tasks = []

    while True:
        print("\n===== TO-DO MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Done")
        print("0. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter task title: ").strip()
            desc = input("Enter task description: ").strip()
            
            # Validation: Ensure both title and description are provided
            if title and desc:
                # Store as [Title, Status, Description]
                tasks.append([title, False, desc])
                print(f"Task '{title}' added successfully!")
            else:
                print("Error: Both Title and Description are required!")

        elif choice == '2':
            show_tasks(tasks)

        elif choice == '3':
            if not tasks:
                print("Nothing to remove/empty.")
                continue
            show_tasks(tasks)
            idx = get_valid_index(tasks, "Enter the task number to REMOVE: ")
            removed = tasks.pop(idx)
            print(f"Removed: {removed[0]}")

        elif choice == '4':
            if not tasks:
                print("No tasks to mark/empty.")
                continue
            show_tasks(tasks)
            idx = get_valid_index(tasks, "Enter the task number to mark as DONE: ")
            tasks[idx][1] = True
            print(f"Updated: {tasks[idx][0]} is now marked as done!")

        elif choice == '0':
            print("Exiting. Have a productive day!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()