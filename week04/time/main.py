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
