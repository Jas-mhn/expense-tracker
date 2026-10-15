"""
Expense Tracker
A simple console application to record, view, and total daily expenses.
Data is saved in a JSON file so it is not lost when the program closes.
"""

import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    """Read saved expenses from the file. Return an empty list if none exist."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    """Write the list of expenses to the file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Ask the user for details and add a new expense."""
    date = input("Enter date (DD-MM-YYYY): ").strip()
    category = input("Enter category (food, travel, etc.): ").strip().title()

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    note = input("Enter a short note: ").strip()

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    """Print all expenses in a neat table."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n{:<4} {:<12} {:<12} {:>10}  {}".format("No.", "Date", "Category", "Amount", "Note"))
    print("-" * 55)
    for number, expense in enumerate(expenses, start=1):
        print("{:<4} {:<12} {:<12} {:>10.2f}  {}".format(
            number,
            expense["date"],
            expense["category"],
            expense["amount"],
            expense["note"],
        ))


def view_total(expenses):
    """Show the overall total and the total for each category."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)
    print("\nTotal spent: Rs. {:.2f}".format(total))

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]

    print("\nSpending by category:")
    for category, amount in category_totals.items():
        print("  {:<12} Rs. {:.2f}".format(category, amount))


def main():
    """Show the menu and run the program until the user exits."""
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View total spending")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()