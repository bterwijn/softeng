#!/bin/bash
cd ./1_object_oriented/assignments ; pytest -q --tb=no test_alarm_clock.py ; cd -
cd ./1_object_oriented/assignments ; pytest -q --tb=no test_event.py ; cd -
cd ./1_object_oriented/assignments ; pytest -q --tb=no test_time.py ; cd -
cd ./2_polymorphism/assignments ; pytest -q --tb=no test_game_composition.py ; cd -
cd ./3_lazy_evaluation/assignment ; pytest -q --tb=no test_lazy.py ; cd -
