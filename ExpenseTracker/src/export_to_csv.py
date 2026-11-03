import csv
import json
from tracking import choose_expense_file

expense_file = choose_expense_file()
def export_to_csv(expense_file):
    expenses = json.load(expense_file)
    