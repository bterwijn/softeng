from datetime import datetime
import sys
import os
import csv

def main():
    # default command line argument values
    filename = 'expenses.csv'
    command = "list"
    amount = "0.00"
    description = "Not Specified"
    category = None
    date = None

    if len(sys.argv)>1:
        if sys.argv[1] in ['-h', '--help']:
            print_help()
            sys.exit(0) # exit without error
    
    if len(sys.argv)>1:
        filename = sys.argv[1] # read filename argument
    if len(sys.argv)>2:
        command = sys.argv[2] # read command argument
    
    if os.path.exists(filename):
        expenses = load_expenses(filename) # load expenses from file
    else:
        expenses = [] # start with empty list if filename does not exist
        
    if command == "list":
        if len(sys.argv)>3:
            category = sys.argv[3] # read category argument
        if len(sys.argv)>4:
            date = sys.argv[4] # read date argument
        print(f"===== expenses category:{category} date:{date}")
        list_expenses(expenses, category, date)
    elif command == "total":
        print("total:", total_expenses(expenses, category, date))
    elif command == "add":
        if category is None:
            category = "Miscellaneous"
        if date is None:
            date = get_current_date()
        add_expense(expenses, amount, description, category, date)
        if not filename == 'test_expenses.csv': # avoid overwriting test file
            save_expenses(expenses, filename) # save expenses to file

def print_help():
    """ Print help information for program use. """
    print("""usage: python expenses_cli.py [filename='expenses.csv'] [command='list']
Loads the expenses from 'filename' and processes 'command'.

=== command: list
usage: python expenses_cli.py expenses.csv list [category='None'] [date='None']

  Lists all expenses. Filters on 'category' if given, and Filters on 'date'
  if given.
  example: python expenses_cli.py expenses.csv list Food 2000-01-01
    
=== command: total 
usage: python expenses_cli.py expenses.csv total [category='None'] [date='None']

  Prints the total amount of expenses. Filters on 'category' if given, and 
  Filters on 'date' if given.
  example: python expenses_cli.py expenses.csv total Food 2000-01-01
    
=== command: add
usage: python expenses_cli.py expenses.csv add [amount='0.00'] [description='Not Specified'] [category='None'] [date='None']

  Adds an expense with 'amount', 'description', 'category', and 'date', then 
  saves to file. If 'category' is not given it defaults to 'Miscellaneous'.  
  If 'date' is not given it defaults to the current date.
  example: python expenses_cli.py expenses.csv add 5.0 Lunch Food 2025-10-27
""")

def load_expenses(filename):
    """Load expenses from file 'filename' in csv format."""
    expenses = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader) # skip header
        for row in reader:
            if len(row)>0: # skip rows lines
                amount, description, category, date = row
                expenses.append((float(amount), description, category, date))
    return expenses


def save_expenses(expenses, filename):
    """Save 'expenses' to file 'filename' in csv format."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(('amount', 'description', 'category', 'date')) # write header
        for expense in expenses:
            writer.writerow(expense)

# --------------- solution to expenses.py ---------------
            
def add_expense(expenses: list[tuple], amount: float, description: str, 
                category: str="Miscellaneous", date: str=None):
    if date is None:
        date = get_current_date()
    expenses.append((amount, description, category, date))

def filter_expenses(expenses: list[tuple], category: str, date: str):
    return [expense for expense in expenses
            if expense[0] >= 0 and                              # filter out negative amounts 
               (category is None or expense[2] == category) and # filter on category
               (date is None or expense[3] >=date) ]            # filter on date
    
def list_expenses(expenses: list[tuple], category: str=None, date: str=None):
    filtered_expenses = filter_expenses(expenses, category, date)
    filtered_expenses.sort(key = lambda expense: expenses[3]) # sort expenses by date
    for amount, description, category, date in filtered_expenses:
        print(f'{amount:6} {description:20} {category:20} {date:10}')

def total_expenses(expenses: list[tuple], category: str=None, date: str=None):
    filtered_expenses = filter_expenses(expenses, category, date)
    return sum([amount for amount, _, _, _ in filtered_expenses]) # sum all amounts

def get_current_date():
    """Returns the current date in YYYY-MM-DD string format."""
    return datetime.today().strftime("%Y-%m-%d")

if __name__ == "__main__":
    main()
