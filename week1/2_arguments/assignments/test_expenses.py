from softeng import fixedhash, replace_fixedhash
import pytest
import os, sys, io
import expenses as exp

def test_add_expense():
    expenses = []
    exp.add_expense(expenses, 10.50, "Lunch", "Food", "2022-03-21")
    exp.add_expense(expenses,  3.50, "Pencils, Tape")
    exp.add_expense(expenses, 18.00, "Groceries", date=exp.get_current_date())
    exp.add_expense(expenses, 17.50, "Dinner", date=exp.get_current_date(), category="Food")
    # description
    assert expenses[0][1] == "Lunch"
    assert expenses[1][1] == "Pencils, Tape"
    assert expenses[2][1] == "Groceries"
    assert expenses[3][1] == "Dinner"
    # category
    assert expenses[0][2] == "Food"
    assert expenses[1][2] == "Miscellaneous"
    assert expenses[2][2] == "Miscellaneous"
    assert expenses[3][2] == "Food"
    # date
    assert expenses[0][3] < "2025-01-01"
    assert expenses[1][3] > "2025-01-01"
    assert expenses[2][3] > "2025-01-01"
    assert expenses[3][3] > "2025-01-01"
    
def helper_list_expenses(expenses: list[tuple], category: str=None, date: str=None):
    old_stdout = sys.stdout      # Save the current stdout
    sys.stdout = io.StringIO()   # Redirect stdout to a StringIO object
    try:
        exp.list_expenses(expenses, category, date)
        output = sys.stdout.getvalue()  # Get the printed output as a string
    finally:
        sys.stdout = old_stdout  # Restore original stdout
    return output.splitlines()

def test_list_expenses():
    expenses = []
    exp.add_expense(expenses, 10.50, "Lunch", "Food", "2022-03-21")
    exp.add_expense(expenses,  3.50, "Pencils, Tape")
    exp.add_expense(expenses, 18.00, "Groceries", date=exp.get_current_date())
    exp.add_expense(expenses, 17.50, "Dinner", date=exp.get_current_date(), category="Food")
    output = helper_list_expenses(expenses, category="Food")
    assert len(output) == 2, "expected 2 'Food' expenses"
    output = helper_list_expenses(expenses, category="Miscellaneous")
    assert len(output) == 2, "expected 2 'Miscellaneous' expenses"
    output = helper_list_expenses(expenses, date="2023-01-01")
    assert len(output) == 3, "expected 3 expenses in 2023 onwards"
    output = helper_list_expenses(expenses)
    for s in [str(10.50), "Lunch", "Food", "2022-03-21"]:
        assert (s in output[0]) == True, f"expected '{s}' in first line"

def test_total_expenses():
    expenses = []
    exp.add_expense(expenses, 10.50, "Lunch", "Food", "2022-03-21")
    exp.add_expense(expenses,  3.50, "Pencils, Tape")
    exp.add_expense(expenses, 18.00, "Groceries", date=exp.get_current_date())
    exp.add_expense(expenses, 17.50, "Dinner", date=exp.get_current_date(), category="Food")
    assert exp.total_expenses(expenses) == pytest.approx(10.50 + 3.50 + 18.00 + 17.50)
    assert exp.total_expenses(expenses, category="Food") == pytest.approx(10.50 + 17.50)
    assert exp.total_expenses(expenses, category="Miscellaneous") == pytest.approx(3.50 + 18.00)
    assert exp.total_expenses(expenses, date="2023-01-01") == pytest.approx(3.50 + 18.00 + 17.50)
