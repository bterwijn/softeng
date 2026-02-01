from softeng import fixedhash, replace_fixedhash
import pytest
import shutil
import expenses_cli as exp_cli

def test_list_expenses(monkeypatch, capsys):
    test_file = "test_expenses.csv"
    monkeypatch.setattr("sys.argv", ['', test_file, "list"])
    exp_cli.main()
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 5, f"expected 5 lines running:  python expenses_cli.py test_expenses.csv list"
    assert 'Lunch' in output[1], f"expected 'Lunch' on second line running:  python expenses_cli.py test_expenses.csv list"
    assert 'Food' in output[1], f"expected 'Food' on second line running:  python expenses_cli.py test_expenses.csv list"
    assert '2022-03-21' in output[1], f"expected '2022-03-21' on second line running:  python expenses_cli.py test_expenses.csv list"

def test_list_expenses_category(monkeypatch, capsys):
    test_file = "test_expenses.csv"
    monkeypatch.setattr("sys.argv", ['', test_file, "list", "Food"])
    exp_cli.main()
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 3, "expected 3 lines running:  python expenses_cli.py test_expenses.csv list Food"
    assert '=====' in output[0], "expected '=====' at first line running:  python expenses_cli.py test_expenses.csv list Food"
    assert 'Lunch' in output[1], "expected 'Lunch' at second line running:  python expenses_cli.py test_expenses.csv list Food"
    assert 'Dinner' in output[2], "expected 'Dinner' at second line running:  python expenses_cli.py test_expenses.csv list Food"

def test_list_expenses_category_date(monkeypatch, capsys):
    test_file = "test_expenses.csv"
    monkeypatch.setattr("sys.argv", ['', test_file, "list", "Food", "2024-01-01"])
    exp_cli.main()
    output = capsys.readouterr().out.splitlines()
    assert len(output) == 2, "expected 2 lines running:  python expenses_cli.py test_expenses.csv list Food 2024-01-01"
    assert 'Dinner' in output[1], "expected 'Dinner' at second line running:  python expenses_cli.py test_expenses.csv list Food 2024-01-01"
    assert '2024-03-16' in output[1], "expected '2024-03-16' at second line running:  python expenses_cli.py test_expenses.csv list Food 2024-01-01"

def test_total_expenses_category(monkeypatch, capsys):
    test_file = "test_expenses.csv"
    monkeypatch.setattr("sys.argv", ['', test_file, "total", "Food"])
    exp_cli.main()
    output = capsys.readouterr().out
    assert 'total' in output, "expected 'total' running:  python expenses_cli.py test_expenses.csv total Food"
    assert '28.0' in output, "expected '28.0' running:  python expenses_cli.py test_expenses.csv total Food"

def test_total_expenses_category_date(monkeypatch, capsys):
    test_file = "test_expenses.csv"
    monkeypatch.setattr("sys.argv", ['', test_file, "total", "Food", "2024-01-01"])
    exp_cli.main()
    output = capsys.readouterr().out
    output_split = output.splitlines()
    assert 'total' in output, "expected 'total' running:  python expenses_cli.py test_expenses.csv total Food 2024-01-01"
    assert '17.5' in output, "expected '17.5' running:  python expenses_cli.py test_expenses.csv total Food 2024-01-01"

def test_add_expense(monkeypatch, capsys):
    org_file = "test_expenses.csv"
    test_file = "test_expenses_temp.csv"
    shutil.copy(org_file, test_file) # copy the original test_expenses.csv file    
    monkeypatch.setattr("sys.argv", ['', test_file, "add"])
    exp_cli.main()
    monkeypatch.setattr("sys.argv", ['', test_file, "add", "100.0", "DESCRIPTION"])
    exp_cli.main()
    monkeypatch.setattr("sys.argv", ['', test_file, "add", "100.0", "DESCRIPTION", "CATEGORY", "DATE"])
    exp_cli.main()
    monkeypatch.setattr("sys.argv", ['', test_file, "list"])
    exp_cli.main()
    commands=f'''
cp test_expenses.csv test_expenses_temp.csv
python expenses_cli.py test_expenses_temp.csv add
python expenses_cli.py test_expenses_temp.csv add 100.0 DESCRIPTION
python expenses_cli.py test_expenses_temp.csv add 100.0 DESCRIPTION DATE
python expenses_cli.py test_expenses_temp.csv list
'''
    output = capsys.readouterr().out
    output_split = output.splitlines()
    assert len(output_split) == 8, f"expected 8 lines with:" + commands
    assert output.count('Not Specified') == 1, f"expected 1x 'Not Specified' with:" + commands
    assert output.count('DESCRIPTION') == 2, f"expected 2x 'DESCRIPTION' with:" + commands
    assert output.count('DATE') == 1, f"expected 1x 'DATE' with:" + commands
