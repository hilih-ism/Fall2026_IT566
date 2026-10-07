
from datetime import datetime
def create_diary_entry(filename):
 entry_text = input("Write Today's entry: ")
 entry_date = datetime.now().strftime("%Y-%m-%d")
 
 diary_entry = f"{entry_date} | {entry_text}\n"
 
 with open(filename, "a") as diary_file:
    diary_file.write(diary_entry)

#  return diary_entry
def choose_diary_file():
    filename = input("Enter diary filename: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    return filename

# def filter_entries_by_date(filename):