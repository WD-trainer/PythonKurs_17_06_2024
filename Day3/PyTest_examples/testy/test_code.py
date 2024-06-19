import pytest  # pip install pytest


from Day3.PyTest_examples.code_pytest import sumuj, dajCyfry


def test_sumuj():
    assert sumuj(5, 3) == 8


def test_dajCyfryMin():
    tab = dajCyfry()
    assert min(tab) == 1


def test_dajCyfryMax():
    tab = dajCyfry()
    assert max(tab) == 10


def test_dajCyfryLen():
    tab = dajCyfry()
    assert len(tab) == 10