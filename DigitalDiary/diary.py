
from datetime import datetime
def create_diary_entry():
 entry_text = input("Write Today's entry: ")
 entry_date = datetime.now()
 entry_date = datetime.now().strftime("%Y-%m-%d")
 diary_entry = f"{entry_date} | {entry_text}\n"
#  with open("diary.txt", "a") as diary_file:
#     diary_file.write(diary_entry)

 return diary_entry