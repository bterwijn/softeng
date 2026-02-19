import pytest
from alarm_clock import Time


def test_to_string():
    assert str(Time(23, 59, 59)) == "23:59:59"
    assert str(Time(0, 0, 0)) == "00:00:00"
    assert str(Time(1, 2, 3)) == "01:02:03"


def test_time_get_hours_minutes_seconds():
    assert Time(23, 59, 59).get_hours() == 23
    assert Time(23, 59, 59).get_minutes() == 59
    assert Time(23, 59, 59).get_seconds() == 59
    assert Time(1, 2, 3).get_hours() == 1
    assert Time(1, 2, 3).get_minutes() == 2
    assert Time(1, 2, 3).get_seconds() == 3


def test_time_set_time_positive():
    time = Time(0, 0, 0)
    time.set_time(1, 2, 3)
    assert str(time) == "01:02:03"
    time.set_time(0, 0, 61)
    assert str(time) == "00:01:01"
    time.set_time(0, 61, 0)
    assert str(time) == "01:01:00"
    time.set_time(25, 0, 0)
    assert str(time) == "01:00:00"
    time.set_time(0, 0, 120)
    assert str(time) == "00:02:00"
    time.set_time(0, 120, 0)
    assert str(time) == "02:00:00"


def test_time_set_time_negative():
    assert str(Time(0, 1, -1)) == "00:00:59"
    assert str(Time(1, -1, 0)) == "00:59:00"
    assert str(Time(-1, 0, 0)) == "23:00:00"
    assert str(Time(0, 0, -1)) == "23:59:59"
    assert str(Time(0, 2, -120)) == "00:00:00"
    assert str(Time(0, -30, 0)) == "23:30:00"
    assert str(Time(0, -90, 0)) == "22:30:00"
    assert str(Time(-47, 0, 0)) == "01:00:00"


def test_time_set_time_positive():
    time = Time(0, 0, 0)
    time.set_time(0, 1, -1)
    assert str(time) == "00:00:59"
    time.set_time(1, -1, 0)
    assert str(time) == "00:59:00"
    time.set_time(-1, 0, 0)
    assert str(time) == "23:00:00"
    time.set_time(0, 0, -1)
    assert str(time) == "23:59:59"
    time.set_time(0, 2, -120)
    assert str(time) == "00:00:00"
    time.set_time(0, -30, 0)
    assert str(time) == "23:30:00"
    time.set_time(0, -90, 0)
    assert str(time) == "22:30:00"
    time.set_time(-47, 0, 0)
    assert str(time) == "01:00:00"


def test_time_get_total_seconds():
    assert Time(0, 0, 0).get_total_seconds() == 0
    assert Time(0, 0, 1).get_total_seconds() == 1
    assert Time(0, 1, 0).get_total_seconds() == 60
    assert Time(1, 0, 0).get_total_seconds() == 60 * 60
    assert Time(1, 1, 1).get_total_seconds() == 60 * 60 + 60 + 1
    assert Time(23, 59, 59).get_total_seconds() == 24 * 60 * 60 - 1
    assert Time(3, 3, 3).get_total_seconds() == 3 * 60 * 60 + 3 * 60 + 3


def test_time_addition():
    assert str(Time(0, 0, 0) + Time(0, 0, 1)) == "00:00:01"
    assert str(Time(0, 0, 0) + Time(0, 1, 0)) == "00:01:00"
    assert str(Time(0, 0, 0) + Time(1, 0, 0)) == "01:00:00"
    assert str(Time(0, 0, 0) + Time(0, 0, -1)) == "23:59:59"
    assert str(Time(0, 0, 0) + Time(0, -1, 0)) == "23:59:00"
    assert str(Time(0, 0, 0) + Time(-1, 0, 0)) == "23:00:00"
    assert str(Time(0, 0, 0) + Time(0, 0, 60)) == "00:01:00"
    assert str(Time(0, 0, 0) + Time(0, 60, 0)) == "01:00:00"
    assert str(Time(0, 0, 0) + Time(24, 0, 0)) == "00:00:00"
    assert str(Time(23, 59, 59) + Time(0, 0, 0)) == "23:59:59"
    assert str(Time(23, 59, 59) + Time(0, 0, 1)) == "00:00:00"
    assert str(Time(23, 59, 59) + Time(0, 1, 0)) == "00:00:59"
    assert str(Time(23, 59, 59) + Time(1, 0, 0)) == "00:59:59"
    assert str(Time(1, 2, 3) + Time(4, 5, 6)) == "05:07:09"
    assert str(Time(4, 5, 6) + Time(1, 2, 3)) == "05:07:09"


def test_time_subtract():
    assert str(Time(1, 2, 3) - Time(1, 2, 3)) == "00:00:00"
    assert str(Time(0, 0, 1) - Time(0, 0, 0)) == "00:00:01"
    assert str(Time(0, 1, 0) - Time(0, 0, 0)) == "00:01:00"
    assert str(Time(1, 0, 0) - Time(0, 0, 0)) == "01:00:00"
    assert str(Time(1, 2, 4) - Time(1, 2, 3)) == "00:00:01"
    assert str(Time(1, 3, 3) - Time(1, 2, 3)) == "00:01:00"
    assert str(Time(2, 2, 3) - Time(1, 2, 3)) == "01:00:00"
    assert str(Time(1, 2, 2) - Time(1, 2, 3)) == "23:59:59"
    assert str(Time(1, 1, 3) - Time(1, 2, 3)) == "23:59:00"
    assert str(Time(0, 2, 3) - Time(1, 2, 3)) == "23:00:00"
    assert str(Time(16, 15, 14) - Time(13, 12, 11)) == "03:03:03"
    assert str(Time(0, 0, 0) - Time(23, 59, 59)) == "00:00:01"
    assert str(Time(1, 2, 3) - Time(4, 5, 6)) == "20:56:57"
