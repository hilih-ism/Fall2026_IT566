import json
import os


def filter_expenses():
    expense_folder = "ExpenseFiles"

    print("1. Filter by date")
    print("2. Filter by category")
    print("3. Filter by date and category")

    choice = input("Choose a filter option: ")

    search_date = None
    search_category = None

    if choice == "1":
        search_date = input("Enter date (YYYY-MM-DD): ")

    elif choice == "2":
        search_category = input("Enter category: ")

    elif choice == "3":
        search_date = input("Enter date (YYYY-MM-DD): ")
        search_category = input("Enter category: ")

    else:
        print("Invalid choice.")
        return

    found = False

    for filename in os.listdir(expense_folder):
        if filename.endswith(".json"):
            filepath = os.path.join(expense_folder, filename)

            with open(filepath, "r") as expense_file:
                expenses = json.load(expense_file)
                if isinstance(expenses, dict):
                 expenses = [expenses]

            for expense in expenses:
                date_matches = (
                    search_date is None
                    or expense["date"] == search_date
                )

                category_matches = (
                    search_category is None
                    or expense["category"].lower()
                    == search_category.lower()
                )

                if date_matches and category_matches:
                    print(
                        f'{expense["date"]} | '
                        f'{expense["expense"]} | '
                        f'{expense["category"]}'
                    )
                    found = True

    if not found:
        print("No matching expenses found.")