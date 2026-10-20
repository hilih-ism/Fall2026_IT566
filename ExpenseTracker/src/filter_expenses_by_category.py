import os

def filter_expenses_by_category(filename):
   if not os.path.exists(filename):
       print(f"File {filename} does not exist.")
       return
   
   search_category = input("Enter category to filter expenses: ")

   found = False

   with open(filename, "r") as expense_file:
       for line in expense_file:
           if line.endswith(f" | {search_category}\n"):
               print(line, end="")
               found = True

   if not found:
       print(f"No expenses found for category: {search_category}.")