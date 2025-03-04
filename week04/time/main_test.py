import pytest
from unittest.mock import patch, mock_open
from main import Time
import json


@pytest.fixture
def time_object():
    return Time(1, 2, 3)


def test_str(time_object):
    assert str(time_object) == "01:02:03"


def test_add(time_object):
    other_time = Time(4, 5, 6)
    result = time_object + other_time
    assert result.hours == 5
    assert result.minutes == 7
    assert result.seconds == 9


def test_sub(time_object):
    other_time = Time(4, 5, 6)
    result = other_time - time_object
    assert result.hours == 3
    assert result.minutes == 3
    assert result.seconds == 3


def test_total_seconds(time_object):
    assert time_object.total_seconds == 3723


def test_from_string():
    time_object = Time.from_string("01:02:03")
    assert time_object.hours == 1
    assert time_object.minutes == 2
    assert time_object.seconds == 3


def test_from_seconds():
    time_object = Time.from_seconds(3723)
    assert time_object.hours == 1
    assert time_object.minutes == 2
    assert time_object.seconds == 3


@patch("builtins.open", new_callable=mock_open)
def test_save(mock_file, time_object):
    time_object.save("test.json")
    mock_file.assert_called_once_with("test.json", "w")
    mock_file().write.assert_called_once_with(
        json.dumps({"hours": 1, "minutes": 2, "seconds": 3})
    )


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='{"hours": 1, "minutes": 2, "seconds": 3}',
)
def test_load(mock_file):
    time_object = Time.load("test.json")
    assert time_object.hours == 1
    assert time_object.minutes == 2
    assert time_object.seconds == 3


def test_add_hours(time_object):
    time_object.add_hours(4)
    assert time_object.hours == 5


def test_add_minutes(time_object):
    time_object.add_minutes(4)
    assert time_object.minutes == 6


def test_add_seconds(time_object):
    time_object.add_seconds(4)
    assert time_object.seconds == 7
