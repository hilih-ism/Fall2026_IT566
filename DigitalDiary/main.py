from diary import choose_diary_file, create_diary_entry, filter_entries_by_date

def main():
 diary_filename = choose_diary_file()
 while True:
  print()
  print(f"Current diary: {diary_filename}")
  print("1. Create diary entry")
  print("2. View entries by date")
  print("3. Change diary file")
  print("4. Exit")

  choice = input("Choose an option: ")
  if choice == "1":
    create_diary_entry(diary_filename)
  elif choice == "2":
    filter_entries_by_date(diary_filename)
  elif choice == "3":
    diary_filename = choose_diary_file()

  elif choice == "4":
    exit()

  else:
    print("Invalid choice.")

 create_diary_entry(diary_filename)

if __name__ == "__main__":
 main()