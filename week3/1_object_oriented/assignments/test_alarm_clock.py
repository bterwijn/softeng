import pytest
from alarm_clock import Event, Time, AlarmClock, now


def test_add_event():
    alarm_clock = AlarmClock()
    assert len(alarm_clock) == 0
    alarm_clock.add_event(Event(Time(0, 0, 1), "event1"))
    assert len(alarm_clock) == 1
    alarm_clock.add_event(Event(Time(0, 0, 2), "event2"))
    assert len(alarm_clock) == 2
    alarm_clock.add_event(Event(Time(0, 0, 3), "event3"))
    assert len(alarm_clock) == 3
    assert "00:00:01" in str(alarm_clock)
    assert "event1" in str(alarm_clock)
    assert "00:00:02" in str(alarm_clock)
    assert "event2" in str(alarm_clock)
    assert "00:00:03" in str(alarm_clock)
    assert "event3" in str(alarm_clock)
    assert "00:00:04" not in str(alarm_clock)
    assert "event4" not in str(alarm_clock)


def test_sort_get_next_event():
    alarm_clock = AlarmClock()
    alarm_clock.add_event(Event(Time(3, 3, 3), "event333"))
    assert alarm_clock.get_next_event().get_description() == "event333"
    alarm_clock.add_event(Event(Time(3, 3, 9), "event339"))
    assert alarm_clock.get_next_event().get_description() == "event333"
    alarm_clock.add_event(Event(Time(2, 2, 2), "event222"))
    assert alarm_clock.get_next_event().get_description() == "event222"
    alarm_clock.add_event(Event(Time(2, 9, 0), "event290"))
    assert alarm_clock.get_next_event().get_description() == "event222"
    alarm_clock.add_event(Event(Time(1, 1, 1), "event111"))
    assert alarm_clock.get_next_event().get_description() == "event111"
    alarm_clock.add_event(Event(Time(9, 0, 0), "event900"))
    assert alarm_clock.get_next_event().get_description() == "event111"


def test_sort_remove_next_event():
    alarm_clock = AlarmClock()
    secs = [4, 2, 9, 6, 3, 1, 7, 5, 8]
    for i in secs:
        alarm_clock.add_event(Event(Time(0, 0, i), "event" + str(i)))
    assert len(alarm_clock) == len(secs)
    for i in sorted(secs):
        event = alarm_clock.remove_next_event()
        assert event.get_time().get_seconds() == i
        assert event.get_description() == "event" + str(i)
    assert len(alarm_clock) == 0


class Event_Collector:

    def __init__(self):
        self.events = []

    def __call__(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events


def test_wait_and_handle_events():
    alarm_clock = AlarmClock()
    alarm_clock.add_event(Event(now() + Time(0, 0, 2), "event2"))
    alarm_clock.add_event(Event(now() + Time(0, 0, 1), "event1"))
    alarm_clock.add_event(Event(now() + Time(0, 0, 3), "event3"))
    event_collector = Event_Collector()
    alarm_clock.wait_for_and_handle_events(event_collector)
    assert len(event_collector.get_events()) == 3
    assert len(alarm_clock) == 0
    all_events = event_collector.get_events()
    assert "event1" == all_events[0].get_description()
    assert "event2" == all_events[1].get_description()
    assert "event3" == all_events[2].get_description()
