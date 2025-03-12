from Time import Time
import json


class Time_Collection:
    """
    Класс для хранения коллекции объектов Time.
    """

    def __init__(self, *times: Time) -> None:
        """
        Инициализация коллекции объектов Time.
        """
        self._data = []
        for time in times:
            self._data.append(time)

    def __str__(self) -> str:
        """
        Возвращает строковое представление коллекции объектов Time.
        """
        return "Times: {}".format([str(time) for time in self._data])

    def __getitem__(self, index: int) -> Time:
        """
        Возвращает объект Time по индексу.
        """
        return self._data[index]

    def add(self, time: Time) -> None:
        """
        Добавляет объект Time в коллекцию.
        """
        self._data.append(time)
        print(f"Добавлен элемент {time}")

    def remove(self, index: int) -> None:
        """
        Удаляет объект Time из коллекции по индексу.
        """
        self._data.pop(index)
        print(f"Удалён элемент {self._data[index]}")

    def save(self, filename: str) -> None:
        """
        Сохраняет коллекцию объектов Time в JSON-файл.
        """
        times_dict = [time.__dict__ for time in self._data]

        with open(filename, "w") as f:
            f.write(json.dumps({"Times": times_dict}))

    @classmethod
    def load(cls, filename: str):
        """
        Метод класса для загрузки объекта из JSON-файла.
        """
        with open(filename, "r") as file:
            data = json.load(file)
        times = [Time(**time_dict) for time_dict in data["Times"]]
        return cls(*times)
