def choose_expense_file():
    filename = input("Enter expense file name: ")

    if not filename.endswith(".json"):
        filename += ".json"

    return filename