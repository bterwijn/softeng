from softeng import fixedhash, replace_fixedhash
import pytest
import combinatorics as comb

def test_permutation_repetition():
    assert comb.permutation_repetition(3, 2) == 9
    assert comb.permutation_repetition(4, 3) == 64
    assert comb.permutation_repetition(5, 4) == 625

def test_permutation():
    assert comb.permutation(3, 2) == 6
    assert comb.permutation(4, 3) == 24
    assert comb.permutation(5, 4) == 120

def test_combination():
    assert comb.combination(3, 2) == 3
    assert comb.combination(4, 3) == 4
    assert comb.combination(5, 4) == 5

def test_combination_repetition():
    assert comb.combination_repetition(3, 2) == 6
    assert comb.combination_repetition(4, 3) == 20
    assert comb.combination_repetition(5, 4) == 70

def test_question1():
    assert comb.question1() == 26421990030058775793549001827845550530904677327643924414176409107961837701555004459949

def test_question2():
    assert fixedhash(comb.question2()) == "9c65a91aea875853c0b6947137899313f0e72a06cb188bbd6730e61931471143"

def test_question3():
    assert fixedhash(comb.question3()) == "d9d2d34219ade27ebe5981dc4d39172742d80de567247342c21582ad859226c1"

def test_question4():
    assert fixedhash(comb.question4()) == "25974043773b65fda7d13635b98057b61c354f430b4174a83d752b65dabc475f"

def test_question5():
    assert fixedhash(comb.question5()) == "060fc3a6988494d8e218c47717e682bee5da91a2d4841490b5f3b52ba8a679f2"

def test_question6():
    assert fixedhash(comb.question6()) == "1f754da69170e2714c5e0d1c8671c7d1fbfa132c1c6bd16532cf0d31049f8b8a"

def test_question7():
    assert fixedhash(comb.question7()) == "19f27f9a065c016b1bc3238d240f1b24c68ff3d8e646e298d3e6f3f0047033b1"

def test_question8():
    assert fixedhash(comb.question8()) == "4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5"
