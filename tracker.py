#Expense Tracker

expenses = []  # list of all expenses in form of dictionaries
print("welcome to Expense Tracker :")

while True:
    print("----Menu----")
    print("1. Add Expenses")
    print("2. view all Expense")
    print("3. View total expense")
    print("4. Exit")

    choice = int(input("Please enter your choice : "))

    # Add expense
    if choice == 1:
        date = input("Date of expenses? ")
        category = input("Enter the category of expense (Food, Travel, Makeup etc.) : ")
        description = input("Enter details of expense : ")
        amount = float(input("Enter the amount of expense : "))

        expense = {
            "Date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nExpense is successfully added")

    # View all expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No Expenses for now : ")
        else:
            print("This is your expense :")
            count = 1
            for eachexpense in expenses:
                print(
                    f"Expense count {count} -> "
                    f"{eachexpense['Date']}, "
                    f"{eachexpense['category']}, "
                    f"{eachexpense['description']}, "
                    f"{eachexpense['amount']}"
                )
                count = count + 1

    # View total spending
    elif choice == 3:
        total = 0
        for eachexpense in expenses:
            total = total + eachexpense["amount"]
        print("\nTotal expense =", total)

    # Exit
    elif choice == 4:
        print("Thank you for using our tracker")
        break

    else:
        print("Invalid choice try again")
