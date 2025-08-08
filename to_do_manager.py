task_list=[]
def show_main_menu():
    print("\n to_do list menu")
    print("1.add a new task")
    print("2.view all task")
    print("3.update a task")
    print("4.delete a task")
    print("5.exit the application")
def add_task():
    task=input("enter the task:")
    task_list.append(task)
    print("task has been added successfully!")
def view_task():
    if len(task_list)==0:
        print("your to_do list is empty")
    else:
        print("\n here are your tasks:")
        for index,task in enumerate(task_list,start=1):
            print(f"{index}.{task}")
def update_task():
    view_task()
    try:
        number=int(input("enter the task number you want to update:"))
        if 1<=number<=len(task_list):
            new_task=input("enter the updated task:")
            task_list[number-1]=new_task
            print("task has been updated.")
        else:
            print("invalid task number.")
    except:
        print("please enter a valid number.")
def delete_task():
    view_task()
    try:
        number=int(input("enter the task number to delete:"))
        if 1<=number<=len(task_list):
            removed=task_list.pop(number-1)
            print(f"task'{removed}'has been deleted.")
        else:
            print("invalid task number.")
    except:
        print("pkease enter the valid number.")
while True:
    show_main_menu()
    choice=input("select an option(1 to 5):")
    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        update_task()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("thank you!")
    else:
        print("invalid option.please try again.")