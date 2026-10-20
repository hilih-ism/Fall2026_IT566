import os

def filter_expenses_by_date(filename):
   if not os.path.exists(filename):
       print(f"File {filename} does not exist.")
       return
   
   search_date = input("Enter date to filter expenses (YYYY-MM-DD): ")

   found = False

   with open(filename, "r") as expense_file:
       for line in expense_file:
           if line.startswith(search_date):
               print(line, end="")
               found = True

   if not found:
       print(f"No expenses found for date: {search_date}.")