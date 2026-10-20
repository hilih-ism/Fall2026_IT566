from tracking import choose_expense_file
from tracking import create_expense_entry
from filter_expenses_by_date import filter_expenses_by_date

def main():
 expense_file = choose_expense_file()
 
 while True:
  print()
  print(f"Current file: {expense_file}")
  print("1. Enter new expenses")
  print("2. filter expenses by date")
  print("3. Change expense file")
  print("4. Exit")

  choice = input("Choose an option: ")
  if choice == "1":
    create_expense_entry(expense_file)
  elif choice == "2":
    filter_expenses_by_date(expense_file)
  elif choice == "3":
    expense_file = choose_expense_file()
  elif choice == "4":
    exit()

  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()