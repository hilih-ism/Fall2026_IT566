from tracking import choose_expense_file
from tracking import create_expense_entry
from filter_expenses import filter_expenses

def main():
 expense_file = choose_expense_file()
 
 while True:
  print()
  print(f"Current file: {expense_file}")
  print("1. Enter new expenses")
  print("2. Filter expenses")
  print("3. Change expense file")
  print("4. Export a file to csv format")
  print("5. Exit")

  choice = input("Choose an option: ")
  if choice == "1":
    create_expense_entry(expense_file)
  elif choice == "2":
    filter_expenses()
  elif choice == "3":
    expense_file = choose_expense_file()
  elif choice == "4":
    export_to_csv(expense_file)
  elif choice == "5":
    exit()

  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()