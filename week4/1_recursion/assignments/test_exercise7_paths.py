import pytest
import softeng

import exercise7_paths

def test_get_all_paths_is_recursive():
    assert softeng.is_recursive(exercise7_paths.get_all_paths), "The function 'get_all_paths()' should be recursive."

def test_generator_of_lists_usage():
    connections = exercise7_paths.edges_to_connections(exercise7_paths.edges)
    generator_function = exercise7_paths.get_all_paths(connections, ['a'], 'b')
    assert hasattr(generator_function, '__iter__') and hasattr(generator_function, '__next__'), "The function should return a generator."
    
    for result in generator_function:
        assert isinstance(result, list), "Each result from the generator should be a list."

def get_paths():
    connections = exercise7_paths.edges_to_connections(exercise7_paths.edges)
    results = []
    generator_function = exercise7_paths.get_all_paths(connections, ['a'], 'b')
    return set([tuple(r) for r in generator_function])  # convert lists to tuples so they are hashable

def test_exercise7_paths():
    paths = get_paths()
    print(paths)
    assert len(paths) == 145
    assert ('a', 'v', 'a', 'v', 'j', 'd', 'p', 'r', 'w', 'b') in paths
    assert ('a', 'h', 'y', 'u', 'd', 'j', 'a', 's', 'k', 'b') in paths
    assert ('a', 'j', 'd', 'j', 'a', 'q', 'a', 's', 'k', 'b') in paths
    assert ('a', 'j', 'v', 'a', 'j', 'd', 'u', 'r', 'w', 'b') in paths
    assert ('a', 'j', 'd', 'j', 'a', 's', 'l', 's', 'k', 'b') in paths
    assert ('a', 'v', 'j', 'i', 'j', 'd', 'j', 'i', 'w', 'b') in paths

def test_exercise7_paths_more():
    paths = get_paths()
    assert {('a', 'h', 'a', 'v', 'j', 'd', 'u', 'r', 'w', 'b'), 
            ('a', 'j', 'd', 'j', 'd', 'j', 'a', 's', 'k', 'b')} < paths
    assert len({('a', 'v', 'j', 'd', 'u', 'r', 'w', 'i', 'w', 'b'),
                ('a', 'v', 'j', 'd', 'p', 'f', 'w', 'b', 'w', 'b'),
                ('a', 'v', 'j', 'd', 'p', 'r', 'p', 'r', 'k', 'b')} & paths) == 1
    assert len(paths - {('a', 's', 'a', 'j', 'd', 'j', 'a', 'm', 'g', 'b'),
                        ('a', 'j', 'v', 'j', 'a', 'd', 'u', 'r', 'w', 'b')}) == 144
