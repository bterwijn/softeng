#!/bin/bash
cd ./1_pruning/assignments ; pytest -q --tb=no test_player_ai_allmove_prune.py ; cd -
cd ./2_depth_heuristic/assignments ; pytest -q --tb=no test_player_ai_dmove_heuristic.py ; cd -
cd ./2_depth_heuristic/assignments ; pytest -q --tb=no test_player_ai_dmove.py ; cd -
cd ./2_depth_heuristic/assignments ; pytest -q --tb=no test_tictactoe_heuristic.py ; cd -
cd ./3_connect_four/assignments ; pytest -q --tb=no test_connect_four_evaluator.py ; cd -
cd ./3_connect_four/assignments ; pytest -q --tb=no test_connect_four_heuristic.py ; cd -
cd ./3_connect_four/assignments ; pytest -q --tb=no test_connect_four.py ; cd -
cd ./4_chess/assignments ; pytest -q --tb=no test_chess_adapter.py ; cd -
