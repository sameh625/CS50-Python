import pytest
from um import count

def test_normal_situation():
    assert count("um, hello, um, world") == 2
    assert count("sameh um... sameh um...") == 2

def test_inside_a_word():
    assert count("yummy") == 0
    assert count("yum") == 0

def test_case_insensitive():
    assert count("UM, hello, UM...") == 2
