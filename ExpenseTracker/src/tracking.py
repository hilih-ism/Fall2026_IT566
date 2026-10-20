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
 entry_text = input("Enter your expense: ")
 entry_category = input("Choose a category: ")
 while True:
        entry_date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.datetime.strptime(entry_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")

 expense_entry = {
        "date": entry_date,
        "expense": entry_text,
        "category": entry_category
    }

 with open(filepath, "w") as expense_file:
        json.dump(expense_entry, expense_file, indent=4)