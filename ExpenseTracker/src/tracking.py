import datetime
import json
import os


def choose_expense_file():
    filename = input("Enter expense file name: ")

    if not filename.endswith(".json"):
        filename += ".json"
    filepath = os.path.join("ExpenseFiles", filename)
    return filepath


def create_expense_entry(filepath):
    while True:
        try:
            entry_expense = int(input("Enter your expense: "))
            break
        except ValueError:
            print("Invalid expense. Enter a whole number.")

    while True:
        entry_category = input("Choose a category: ").strip()

        if entry_category.isalpha():
            break
        else:
            print("Invalid category. Enter letters only.")

    while True:
        entry_date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.datetime.strptime(entry_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")

    expense_entry = {
        "date": entry_date,
        "expense": entry_expense,
        "category": entry_category
    }

    if os.path.exists(filepath):
        with open(filepath, "r") as expense_file:
            expenses = json.load(expense_file)
    else:
        expenses = []

    expenses.append(expense_entry)

    with open(filepath, "w") as expense_file:
        json.dump(expenses, expense_file, indent=4)

    print(
        f"Added expense: {entry_expense} "
        f"in category: {entry_category} "
        f"on date: {entry_date}"
    )