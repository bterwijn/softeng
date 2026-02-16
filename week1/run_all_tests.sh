#!/bin/bash
cd ./1_setup/assignments ; pytest -q --tb=no test_addition.py ; cd -
cd ./1_setup/assignments ; pytest -q --tb=no test_file_python_venv_png.py ; cd -
cd ./2_arguments/assignments ; pytest -q --tb=no test_expenses_cli.py ; cd -
cd ./2_arguments/assignments ; pytest -q --tb=no test_expenses.py ; cd -
cd ./3_packages/assignments ; pytest -q --tb=no test_approximate.py ; cd -
cd ./3_packages/assignments ; pytest -q --tb=no test_combinatorics.py ; cd -
