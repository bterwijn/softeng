import pytest
import softeng

import exercise6_paths

def test_palindromes_is_recursive():
    assert softeng.is_recursive(exercise6_paths.get_all_paths), "The function 'get_all_paths()' should be recursive."

def test_list_usage():
    connections = exercise6_paths.edges_to_connections(exercise6_paths.edges)
    results = []
    exercise6_paths.get_all_paths(connections, ['a'], 'b', results)
    for result in results:
        assert isinstance(result, list), "Results should be a list (or iterable) of lists."

def get_paths():
    connections = exercise6_paths.edges_to_connections(exercise6_paths.edges)
    results = []
    exercise6_paths.get_all_paths(connections, ['a'], 'b', results)
    return set([tuple(r) for r in results])  # convert lists to tuples so they are hashable

def test_exercise6_paths():
    paths = get_paths()
    print(paths)
    assert len(paths) == 145
    assert ('a', 'v', 'a', 'v', 'j', 'd', 'p', 'r', 'w', 'b') in paths
    assert ('a', 'h', 'y', 'u', 'd', 'j', 'a', 's', 'k', 'b') in paths
    assert ('a', 'j', 'd', 'j', 'a', 'q', 'a', 's', 'k', 'b') in paths
    assert ('a', 'j', 'v', 'a', 'j', 'd', 'u', 'r', 'w', 'b') in paths
    assert ('a', 'j', 'd', 'j', 'a', 's', 'l', 's', 'k', 'b') in paths
    assert ('a', 'v', 'j', 'i', 'j', 'd', 'j', 'i', 'w', 'b') in paths

def test_exercise6_paths_more():
    paths = get_paths()
    assert {('a', 'h', 'a', 'v', 'j', 'd', 'u', 'r', 'w', 'b'), 
            ('a', 'j', 'd', 'j', 'd', 'j', 'a', 's', 'k', 'b')} < paths
    assert len({('a', 'v', 'j', 'd', 'u', 'r', 'w', 'i', 'w', 'b'),
                ('a', 'v', 'j', 'd', 'p', 'f', 'w', 'b', 'w', 'b'),
                ('a', 'v', 'j', 'd', 'p', 'r', 'p', 'r', 'k', 'b')} & paths) == 1
    assert len(paths - {('a', 's', 'a', 'j', 'd', 'j', 'a', 'm', 'g', 'b'),
                        ('a', 'j', 'v', 'j', 'a', 'd', 'u', 'r', 'w', 'b')}) == 144
