import sys
import pytest


def test_pytest_installed():
    assert "pytest" in sys.modules
