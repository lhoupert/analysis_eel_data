import pytest
from analysis_eel_data.dummy import dummy_foo


def test_dummy():
    assert dummy_foo(4) == (4 + 4)
