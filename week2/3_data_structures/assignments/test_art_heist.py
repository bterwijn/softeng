import pytest
import csv
import softeng


@pytest.fixture(scope="session", autouse=True)
def run_art_heist_once():
    import art_heist
    art_heist.main()

def run_art_heist(config):
    import art_heist
    art_heist.main()

def strip_list(input_list):
    return [item.strip() for item in input_list]

def load_data(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = strip_list(next(csv_reader)) # skip header
        data = [strip_list(row) for row in csv_reader if row]
        return header, data
    
def test_art_heist_file():
    try:
        header, data = load_data('daders.csv')
        assert header and header == ['id', 'naam'], 'Header should be correct'
        assert len(data) == 2700, 'There should be 2700 ids in the file'
    except Exception as e:
        assert False, f'Error loading file "daders.csv": {e}'

def test_art_heist_first_last():
    header, data = load_data('daders.csv')
    data.sort()
    assert data and data[0] == ['1001842168', 'Sill Hemelrijk'] , 'Incorrect lowest id'
    assert data and data[-1] == ['9998389118', 'Dana Leerdam'] , 'Incorrect heighest id'

def test_art_heist_all():
    header, data = load_data('daders.csv')
    data.sort()
    ids_string = ''.join(str(id) for id, name in data)
    names_string = ''.join(name for id, name in data)
    assert softeng.fixedhash(ids_string) == "b45716f734a18ac3ca7ee9f56f89014dfd7510cc87dff1b164c246eee23ae2f0", "ids don't match"
    assert softeng.fixedhash(names_string) == "e6528a8d5989f9a6afb3ed37ea6075a773bd061765389ace8256a1c9e6dc2e71", "names don't match"
