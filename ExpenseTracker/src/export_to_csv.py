import csv
import json
import os
from tracking import choose_expense_file


expense_file = choose_expense_file()

def export_to_csv(expense_file):
    current_dir = os.path.dirname(__file__)
    csv_folder = os.path.join(current_dir, "CsvExpenseFiles")

    os.makedirs(csv_folder, exist_ok=True)

    csv_filename = os.path.basename(expense_file).replace(".json", ".csv")
    with open(expense_file, "r") as file:
     expenses = json.load(file)
    with open(csv_filepath, "w", newline="") as csv_file:
     fieldnames = ["date", "expense", "category"]
     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)