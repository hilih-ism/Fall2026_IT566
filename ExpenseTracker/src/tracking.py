import datetime


def choose_expense_file():
    filename = input("Enter expense file name: ")

    if not filename.endswith(".json"):
        filename += ".json"

    return filename

def create_expense_entry(filename):
 entry_text = input("enter your expense: ")
 entry_category = input("choose a category: ")
 entry_date = datetime.datetime.now().strftime("%Y-%m-%d")
 
 expense_entry = f"{entry_date} | {entry_text} | {entry_category}\n"
 
 with open(filename, "a") as expense_file:
    expense_file.write(expense_entry)