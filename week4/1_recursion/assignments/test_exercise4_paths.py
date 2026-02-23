import pytest
import softeng

import exercise4_paths

def test_palindromes_is_recursive():
    assert softeng.is_recursive(exercise4_paths.print_all_paths), "The function 'print_all_paths()' should be recursive."

def get_paths():
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    connections = exercise4_paths.edges_to_connections(exercise4_paths.edges)
    exercise4_paths.print_all_paths(connections, 'a', 'b')
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip().split('\n')
    return set(output)

def test_exercise4_paths():
    paths = get_paths()
    assert len(paths) == 114
    assert 'ajaslkb' in paths
    assert 'ahahyxb' in paths
    assert 'aoavjxb' in paths
    assert 'asajixb' in paths
    assert 'avjxbeb' in paths
    assert 'asaslkb' in paths

def test_exercise4_paths_more():
    paths = get_paths()
    assert {'asajixb', 'aoahyxb', 'ahyxbxb'} < paths
    assert len({'ajdpreb', 'ajixjxb', 'ajiwrub'} & paths) == 1
    assert len(paths - {'avjdjxb', 'aoajixb', 'ajiwbub'}) == 112
