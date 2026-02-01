from datetime import datetime

def main():
    expenses = [] # list of expenses as tuples (amount, description, category, date)

    add_expense(expenses, 10.50, "Lunch",      "Food",          "2022-03-21")
    add_expense(expenses, 17.50, "Dinner",     "Food",          "2022-03-21")

    add_expense(expenses,  8.00, "Breakfast",  "Food",          "2022-03-22")
    add_expense(expenses, 25.00, "Groceries",  "Miscellaneous", "2022-03-22")

    add_expense(expenses, 12.50, "Lunch",      "Food",          "2022-03-23")
    add_expense(expenses, 15.00, "Movie",      "Entertainment", "2022-03-23")

    add_expense(expenses, 31.00, "Groceries",  "Miscellaneous", "2022-03-24")
    add_expense(expenses, 19.00, "Dinner",     "Food",          "2022-03-24")

    print(f'===== list all expenses:')
    list_expenses(expenses)
    print('total:', total_expenses(expenses))

    # # use as test after adding default argument values to add_expense() 
    # add_expense(expenses,  3.50, "Pencils, Tape")
    # add_expense(expenses, 18.00, "Groceries", date=get_current_date())
    # add_expense(expenses, 17.50, "Dinner", date=get_current_date(), category="Food")

    # # use as test after adding 'category' to list_expenses() and total_expenses()
    # print(f'===== Miscellaneous expenses:')
    # list_expenses(expenses, category="Miscellaneous")
    # print('total:', total_expenses(expenses, category="Miscellaneous"))

    # # use as test after adding 'date' to list_expenses() and total_expenses()
    # print(f'===== Food expenses 2023 onwards:')
    # list_expenses(expenses, category="Food", date="2023-01-01")
    # print('total:', total_expenses(expenses, category="Food", date="2023-01-01"))
    # print(f'===== all expenses 2023 onwards:')
    # print('total:', total_expenses(expenses, date="2023-01-01"))
    


def add_expense(expenses: list[tuple], amount: float, description: str, 
                category: str, date: str):
    """Add an expense to 'expenses' as a tuple with 'amount', 'description',
    'category' and 'date'.
    """
    expenses.append((amount, description, category, date)) # append as tuple


def list_expenses(expenses: list[tuple]):
    """List all 'expenses' with positive amount, sorted by date.
    """
    filtered_expenses = filter_expenses(expenses)
    filtered_expenses.sort(key = lambda expense: expenses[3]) # sort expenses by date
    for amount, description, category, date in filtered_expenses:
        print(f'{amount:6} {description:20} {category:20} {date:10}')


def total_expenses(expenses: list[tuple]):
    """Sum all amounts of 'expenses' with positive amount. """
    filtered_expenses = filter_expenses(expenses)
    return sum([amount for amount, _, _, _ in filtered_expenses]) # sum all amounts


def filter_expenses(expenses: list[tuple]):
    """Returns a list of expenses negative amounts filterd out. """
    return [expense for expense in expenses
            if expense[0] >= 0 ] # filter out negative amounts 


def get_current_date():
    """Returns the current date in YYYY-MM-DD string format."""
    return datetime.today().strftime("%Y-%m-%d")


if __name__ == '__main__':
    main()

