# expense tracker 
def main():
    total = 0 
    while True:
        user_input = input("Enter Expense or enter exit for quit: ")
        if user_input == "exit":
            break
        try:
            total = total + int(user_input) 
        except Exception as e:
            print(e)
    print("total expenses: " , total)
    
if __name__ == "__main__":
    main()