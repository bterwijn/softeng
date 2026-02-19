import pytest
from alarm_clock import Event, Time


def test_event():
    time = Time(1, 2, 3)
    description = "hello"
    event = Event(time, description)
    assert str(time) == str(event.get_time())
    assert description == event.get_description()
