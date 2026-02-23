import pytest
import softeng

import exercise5_paths

def test_palindromes_is_recursive():
    assert softeng.is_recursive(exercise5_paths.get_all_paths), "The function 'get_all_paths()' should be recursive."

def get_paths():
    connections = exercise5_paths.edges_to_connections(exercise5_paths.edges)
    results = []
    exercise5_paths.get_all_paths(connections, 'a', 'b', results)
    return set(results)

def test_exercise5_paths():
    paths = get_paths()
    assert len(paths) == 145
    assert 'asavjdprwb' in paths
    assert 'avjdurwbeb' in paths
    assert 'avjdjiwbeb' in paths
    assert 'ajdjavamgb' in paths
    assert 'ajajdjaskb' in paths
    assert 'ajdjdjamgb' in paths

def test_exercise5_paths_more():
    paths = get_paths()
    assert {'avjdjiwbkb', 'ajdjavaskb', 'avjdjiziwb'} < paths
    assert len({'avtjdjaskb', 'avjdpdjiwb', 'asavjduywb'} & paths) == 1
    assert len(paths - {'ajdjamgbkb', 'amavjdjiwb', 'aqajdiaskb'}) == 143
