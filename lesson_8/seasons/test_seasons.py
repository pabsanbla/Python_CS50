from seasons import check
from datetime import datetime
import pytest

def test_check():
    assert check("2023-02-28") == datetime(2023, 2, 28).date()
    assert check("1823-12-02") == datetime(1823, 12, 2).date()
    with pytest.raises(SystemExit):
        check("January 1, 1999")
        check("2014/02/03")
        check("01-02-2015")
