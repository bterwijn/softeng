#!/bin/bash
cd ./1_exceptions/assignments ; pytest -q --tb=no test_grade1.py ; cd -
cd ./1_exceptions/assignments ; pytest -q --tb=no test_grade2.py ; cd -
cd ./1_exceptions/assignments ; pytest -q --tb=no test_grade3.py ; cd -
cd ./2_data_model/assignments ; pytest -q --tb=no test_band_schedule.py ; cd -
cd ./2_data_model/assignments ; pytest -q --tb=no test_products.py ; cd -
cd ./3_data_structures/assignments ; pytest -q --tb=no test_art_heist.py ; cd -
cd ./3_data_structures/assignments ; pytest -q --tb=no test_birthday_match_obfus.py ; cd -
