"""Test Kata 03

numbers.csv taken from:
https://www.tuomas.salste.net/doc/roman/numeri-romani-1-5000.html
"""
import csv
import random
from pathlib import Path

import kata03 as kata
import pytest

csvfile = Path(__file__).parent.resolve() / "numbers.csv"
with csvfile.open() as f:
    reader = csv.reader(f)
    data = [row for row in reader]

long_test = pytest.mark.parametrize("arabic, roman", data)
short_test = pytest.mark.parametrize("arabic, roman", random.sample(data, 20))


@pytest.mark.slow
@long_test
def test_to_roman_all(arabic, roman):
    assert kata.roman(int(arabic)) == roman


@pytest.mark.slow
@long_test
def test_to_arabic_all(arabic, roman):
    assert kata.arabic(roman) == int(arabic)


@short_test
def test_to_roman(arabic, roman):
    assert kata.roman(int(arabic)) == roman


@short_test
def test_to_arabic(arabic, roman):
    assert kata.arabic(roman) == int(arabic)
