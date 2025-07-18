from seasons import Age
import pytest


def test1():
    assert Age.check_valid("2004-04-08") == True


def test2():
    assert Age.check_valid("20004-20-50") == False
