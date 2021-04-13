"""Test Kata 03

numbers.csv taken from:
https://www.tuomas.salste.net/doc/roman/numeri-romani-1-5000.html
"""
import csv
import random

import kata03 as kata
import pytest

with open("numbers.csv") as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

long_test = pytest.mark.parametrize("arabic, roman", data)
short_test = pytest.mark.parametrize("arabic, roman", random.sample(data, 20))


@long_test
def test_to_roman(arabic, roman):
    assert kata.roman(int(arabic)) == roman


@long_test
def test_to_arabic(arabic, roman):
    assert kata.arabic(roman) == int(arabic)
