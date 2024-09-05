import pytest
from working import convert


def test_correct_hours():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("9:00 AM to 17:00 PM")
        convert("9:60 AM to 5 PM")


def test_no_minutes():
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 8 PM") == "10:30 to 20:00"
    assert convert("6 PM to 12 AM") == "18:00 to 00:00"


def test_format():
    assert convert("12 PM to 5:00 AM") == "12:00 to 05:00"
    assert convert("11:30 PM to 8 AM") == "23:30 to 08:00"
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
        convert("9:60 am to 5 PM")
