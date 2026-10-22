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