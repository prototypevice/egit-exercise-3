# toDoApp.py

tasks = []

def add_task(task):
    if not task or not task.strip():
        print("You didn't input any tasks.\n")
        return
    tasks.append(task)
    print("Task added!\n")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.\n")
    else:
        print("Tasks list:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        
        print("\n")

def remove_task(task_number):
    index = task_number - 1
    if index < 0 or index >= len(tasks):
        print("Invalid task number.\n")
        return
    tasks.pop(index)
    print("Task removed!\n")

def main():
    while True:
        print("To Do App in Python")
        print("===============")
        print("1. Add Tasks")
        print("2. Show Tasks")
        print("3. Remove Tasks")
        print("4. Exit")
        print("===============")
        ch = input("Enter choice: ")
        
        if ch == "1":
            t = input("Enter task: ")
            add_task(t)
        elif ch == "2":
            show_tasks()

        elif ch == "3":
            try:
                n = int(input("Enter task number to remove: "))
                remove_task(n)

            except ValueError:
                print("Please enter a valid number.")

        elif ch == "4":
            print("Thank you for using our program!")
            break
        else:
            print("Wrong choice!")

if __name__ == "__main__":
    main()
