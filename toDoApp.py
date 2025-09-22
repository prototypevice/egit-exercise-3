# toDoApp.py

tasks = []

def add_task(task):
    tasks.append(task)
    print("task added!")

def show_tasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def remove_task(tasknumber):
    tasks.pop(tasknumber)
    print("task removed!!")

def main():
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4. Exit")
        ch = input("Enter choice : ")
        
        if ch == "1":
            t = input("Enter task : ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            n = int(input("Enter task number to remove: "))
            removetask(n)
        elif ch == "4":
            break
        else:
            print("Wrong choice!")

if __name__ == "__main__":
    main()
