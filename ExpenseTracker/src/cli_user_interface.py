from tracking import choose_expense_file
from tracking import create_expense_entry
from filter_expenses import filter_expenses
from export_to_csv import export_to_csv


class CLIUserInterface:

    def __init__(self):
        self.expense_file = None

    def start(self):
        self.expense_file = choose_expense_file()

        while True:
            self.print_menu()
            choice = input("Choose an option: ")
            self.process_choice(choice)

            if choice == "5":
                break

    def print_menu(self):
        print()
        print(f"Current file: {self.expense_file}")
        print("1. Enter new expenses")
        print("2. Filter expenses")
        print("3. Change expense file")
        print("4. Export a file to CSV format")
        print("5. Exit")

    def process_choice(self, choice):
        if choice == "1":
            create_expense_entry(self.expense_file)

        elif choice == "2":
            filter_expenses()

        elif choice == "3":
            self.expense_file = choose_expense_file()

        elif choice == "4":
            export_to_csv(self.expense_file)

        elif choice == "5":
            print("Exiting application.")

        else:
            print("Invalid choice.")