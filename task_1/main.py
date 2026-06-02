# create a todolist task 
my_tasks = []
def add_task(task: str):
    my_tasks.append(task)
def print_all_tasks():
    for task in enumerate(my_tasks):
        print(task)

def main():
    while True:
        user_input = input("Enter the operation you wants to perform (Enter add_task for task   adding , print for print all tasks , exit for exit the program) ")
        if user_input == "add_task":
            task = input("enter task: ")
            add_task(task)
        elif user_input == "print":
            print_all_tasks()
        elif user_input == "exit":
            break
if __name__ == "__main__":
    main()
