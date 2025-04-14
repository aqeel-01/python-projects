

'''
project Expense tracker

1) add a new expense
2) view all expenses
3) search for an expense
4) get total expenses
5) delete an expense
6) save and load expenses from JSON files

'''

import json

EXPENSES_FILE = "expenses.json"

#load expenses from file

def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        # Automatically create the file if it doesn't exist or is corrupted
        with open(EXPENSES_FILE, "w") as file:
            json.dump([], file, indent=4)  # Create an empty file if missing or corrupted
        return []

    

# save expenses to file

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent= 4)


#add a new expense

def add_expense(expenses):
    category = input("Enter expense category (e.g food , rent, transport):  ")
    amount = input("Enter amount:  ")

    try:
        amount = float(amount)
        expenses.append({"category": category, "amount": amount})
        save_expenses(expenses)
        print("✅ Expenses added sucessfully!")
    except:
        print("Invalid amount! please enter a valid number .")


# view all expense

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded!")
        return
    print("\n Expense List: ")
    for idx, expense in enumerate(expenses , start= 1):
        print(f"{idx}. {expense['category']} - ${expense['amount']:.2f}")


# search for an expense

def search_expense(expense):
    keyword = input("Enter category to search :  ").lower()
    found = [e for e in expense if keyword in e["category"].lower()]

    if not found:
        print("❌ No Expense found!")
    else:
        print("\n  search Results: ")
        for expense in found:
            print(f"{expense['category']} - ${expense['amount']}:.2f")


# get total expenses

def total_expense(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\n Total Expenses : ${total:.2f}")


# delete an expense

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("Enter the expense number  to delete:  ")) -1
        if 0 <= index < len(expenses):
            deleted_expense = expenses.pop(index)
            save_expenses(expenses)
            print(f"Expense '{deleted_expense['category']}' deleted sucessfully! ")
        else:
            print(" ❌ Invalid expense number!")
    except ValueError:
        print("❌ please enter a valid number!")


# main menu

def main():
    expenses = load_expenses()
    while True:
        print("\n Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Total Expenses")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Enter your choice:  ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            search_expense(expenses)
        elif choice == "4":
            total_expense(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print(" Exiting Expense Tracker . GoodBye !")
            break
        else:
            print(" ❌ invalid choice ! please enter a number between 1-6")

        
# run the program

if __name__ == "__main__":
    main()

        