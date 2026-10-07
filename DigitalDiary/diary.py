
from datetime import datetime
def create_diary_entry(filename):
 entry_text = input("Write Today's entry: ")
 entry_date = datetime.now()
 entry_date = datetime.now().strftime("%Y-%m-%d")
 
 diary_entry = f"{entry_date} | {entry_text}\n"
 
 with open("filename", "a") as diary_file:
    diary_file.write(diary_entry)

#  return diary_entry