from softeng import fixedhash, replace_fixedhash
import pytest
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

def test_list_expenses(capsys):
    expenses = []
    exp.add_expense(expenses, 10.50, "Lunch", "Food", "2022-03-21")
    exp.add_expense(expenses,  3.50, "Pencils, Tape")
    exp.add_expense(expenses, 18.00, "Groceries", date=exp.get_current_date())
    exp.add_expense(expenses, 17.50, "Dinner", date=exp.get_current_date(), category="Food")
    exp.list_expenses(expenses, category="Food")
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 2, "expected 2 'Food' expenses"
    exp.list_expenses(expenses, category="Miscellaneous")
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 2, "expected 2 'Miscellaneous' expenses"
    exp.list_expenses(expenses, date="2023-01-01")
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 3, "expected 3 expenses in 2023 onwards"
    exp.list_expenses(expenses)
    output = capsys.readouterr().out.splitlines()
    for s in [str(10.50), "Lunch", "Food", "2022-03-21"]:
        assert (s in output[0]) == True, f"expected '{s}' in first line"

def test_total_expenses(capsys):
    expenses = []
    exp.add_expense(expenses, 10.50, "Lunch", "Food", "2022-03-21")
    exp.add_expense(expenses,  3.50, "Pencils, Tape")
    exp.add_expense(expenses, 18.00, "Groceries", date=exp.get_current_date())
    exp.add_expense(expenses, 17.50, "Dinner", date=exp.get_current_date(), category="Food")
    assert exp.total_expenses(expenses) == pytest.approx(10.50 + 3.50 + 18.00 + 17.50)
    assert exp.total_expenses(expenses, category="Food") == pytest.approx(10.50 + 17.50)
    assert exp.total_expenses(expenses, category="Miscellaneous") == pytest.approx(3.50 + 18.00)
    assert exp.total_expenses(expenses, date="2023-01-01") == pytest.approx(3.50 + 18.00 + 17.50)
