import pytest
import random
import types

import lazy
import eager

def test_lazy_get_packages():
    random.seed(0)
    gen = lazy.get_packages()
    assert isinstance(gen, types.GeneratorType), "get_packages() should return a generator"

def test_lazy_compute_volume():
    random.seed(0)
    gen = lazy.get_packages()
    gen = lazy.compute_volume(gen)
    assert isinstance(gen, types.GeneratorType), "compute_volume() should return a generator"

def test_lazy_larger_than():
    random.seed(0)
    gen = lazy.get_packages()
    gen = lazy.compute_volume(gen)
    gen = lazy.larger_than(gen, lazy.MINIMAL_VOLUME)
    assert isinstance(gen, types.GeneratorType), "larger_than() should return a generator"

def test_lazy_fill_trucks():
    random.seed(0)
    gen = lazy.get_packages()
    gen = lazy.compute_volume(gen)
    gen = lazy.larger_than(gen, lazy.MINIMAL_VOLUME)
    gen = lazy.fill_trucks(gen)
    assert isinstance(gen, types.GeneratorType), "fill_trucks() should return a generator"

def test_lazy_get_first_n():
    random.seed(0)
    gen = lazy.get_packages()
    gen = lazy.compute_volume(gen)
    gen = lazy.larger_than(gen, lazy.MINIMAL_VOLUME)
    gen = lazy.fill_trucks(gen)
    first_n = lazy.get_first_n(gen, lazy.NR_TRUCKS)
    trucks = list(first_n)
    assert len(trucks) == lazy.NR_TRUCKS, "get_first_n() should return the specified number of trucks"

def test_trucks():
    random.seed(0)
    trucks_eager = eager.fill_trucks()  # to reset random state
    random.seed(0)
    gen = lazy.get_packages()
    gen = lazy.compute_volume(gen)
    gen = lazy.larger_than(gen, lazy.MINIMAL_VOLUME)
    gen = lazy.fill_trucks(gen)
    gen = lazy.get_first_n(gen, lazy.NR_TRUCKS)
    trucks_lazy = list(gen)
    assert trucks_lazy == trucks_eager, "Lazy and eager implementations should produce the same trucks"
