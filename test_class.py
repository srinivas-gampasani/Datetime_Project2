'''

import datetime
import pytest

from datetime_class import MyDatetime

# Unit tests using pytest

def test_creation_default():
    dt = MyDatetime()
    assert isinstance(dt.date, datetime)

def test_creation_with_args():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.date.year == 2023
    assert dt.date.month == 11
    assert dt.date.day == 28
    assert dt.date.hour == 12
    assert dt.date.minute == 30
    assert dt.date.second == 45

def test_creation_from_iso_format():
    dt = MyDatetime.from_iso_format('2023-11-28T12:30:45Z')
    assert dt.date.year == 2023
    assert dt.date.month == 11
    assert dt.date.day == 28
    assert dt.date.hour == 12
    assert dt.date.minute == 30
    assert dt.date.second == 45

def test_iso_format():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.iso_format() == '2023-11-28T12:30:45Z'

def test_human_readable_format():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.human_readable_format() == '2023-11-28 12:30:45'

def test_validate_date_valid():
    assert MyDatetime.validate_date(2023, 11, 28) is True

def test_validate_date_invalid():
    assert MyDatetime.validate_date(2023, 13, 28) is False

def test_date_difference():
    dt1 = MyDatetime(2023, 11, 28)
    dt2 = MyDatetime(2023, 12, 5)
    assert MyDatetime.date_difference(dt1.date, dt2.date) == 7

def test_weekday_calculation():
    dt = MyDatetime(2023, 11, 28)
    assert MyDatetime.weekday_calculation(dt.date.year, dt.date.month, dt.date.day) == 'Monday'

'''

import pytest
from datetime_class import MyDatetime

# Unit tests using pytest

def test_creation_default():
    dt = MyDatetime()
    assert isinstance(dt, MyDatetime)

def test_creation_with_args():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.date.year == 2023
    assert dt.date.month == 11
    assert dt.date.day == 28
    assert dt.date.hour == 12
    assert dt.date.minute == 30
    assert dt.date.second == 45

def test_creation_from_iso_format():
    dt = MyDatetime.from_iso_format('2023-11-28T12:30:45Z')
    assert dt.date.year == 2023
    assert dt.date.month == 11
    assert dt.date.day == 28
    assert dt.date.hour == 12
    assert dt.date.minute == 30
    assert dt.date.second == 45

def test_iso_format():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.iso_format() == '2023-11-28T12:30:45Z'

def test_human_readable_format():
    dt = MyDatetime(2023, 11, 28, 12, 30, 45)
    assert dt.human_readable_format() == '2023-11-28 12:30:45'

def test_validate_date_valid():
    assert MyDatetime.validate_date(2023, 11, 28) is True

def test_validate_date_invalid():
    assert MyDatetime.validate_date(2023, 13, 28) is False

def test_date_difference():
    dt1 = MyDatetime(2023, 11, 28)
    dt2 = MyDatetime(2023, 12, 5)
    assert MyDatetime.date_difference(dt1.date, dt2.date) == 7

def test_weekday_calculation():
    dt = MyDatetime(2023, 11, 28)
    assert MyDatetime.weekday_calculation(dt.date.year, dt.date.month, dt.date.day) == 'Tuesday'
