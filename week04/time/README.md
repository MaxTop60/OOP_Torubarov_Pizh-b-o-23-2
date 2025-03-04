# Простой класс
## Вариант 4. Класс Time (Время)
```PYTHON
#main.py
import json


class Time:
    """
    Класс для работы со временем.

    Атрибуты:
        hours (int): Часы.
        minutes (int): Минуты.
        seconds (int): Секунды.
    """

    def __init__(
            self, hours: int = 0, minutes: int = 0, seconds: int = 0
            ) -> None:
        self.hours: int = hours
        self.minutes: int = minutes
        self.seconds: int = seconds

    def __str__(self) -> str:
        """
        Метод для получения строкового представления объекта.
        """
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        """
        Метод для сложения двух объектов класса Time.
        """
        total_seconds = self.total_seconds + other.total_seconds
        return Time.from_seconds(total_seconds)

    def __sub__(self, other):
        """
        Метод для вычитания двух объектов класса Time.
        """
        total_seconds = self.total_seconds - other.total_seconds
        return Time.from_seconds(total_seconds)

    @property
    def total_seconds(self) -> int:
        """
        Свойство для получения общего количества секунд.
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_string(cls, str_value: str):
        """
        Метод класса для создания объекта на основании строки.
        """
        hours, minutes, seconds = map(int, str_value.split(":"))
        return cls(hours, minutes, seconds)

    @classmethod
    def from_seconds(cls, seconds: int):
        """
        Метод класса для создания объекта на основании количества секунд.
        """
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return cls(hours, minutes, seconds)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(json.dumps({
                "hours": self.hours,
                "minutes": self.minutes,
                "seconds": self.seconds}))

    @classmethod
    def load(cls, filename: str):
        """
        Метод класса для загрузки объекта из JSON-файла.
        """
        with open(filename, "r") as file:
            data = json.load(file)
        return cls(**data)

    def add_hours(self, hours: int) -> None:
        """
        Метод для добавления часов к объекту.
        """
        self.hours += hours

    def add_minutes(self, minutes: int) -> None:
        """
        Метод для добавления минут к объекту.
        """
        self.minutes += minutes

    def add_seconds(self, seconds: int) -> None:
        """
        Метод для добавления секунд к объекту.
        """
        self.seconds += seconds
```
```PYTHON
#main_test.py
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
```