
import os
from datetime import datetime
def create_diary_entry(filename):
 entry_text = input("Write Today's entry: ")
 entry_date = datetime.now().strftime("%Y-%m-%d")
 
 diary_entry = f"{entry_date} | {entry_text}\n"
 
 with open(filename, "a") as diary_file:
    diary_file.write(diary_entry)

def choose_diary_file():
    filename = input("Enter diary filename: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    return filename

def filter_entries_by_date(filename):
   if not os.path.exists(filename):
       print(f"File {filename} does not exist.")
       return
   
   search_date = input("Enter date to filter entries (YYYY-MM-DD): ")

   found = False

   with open(filename, "r") as diary_file:
       for line in diary_file:
           if line.startswith(search_date):
               print(line, end="")
               found = True

   if not found:
       print(f"No entries found for date {search_date}.")
              