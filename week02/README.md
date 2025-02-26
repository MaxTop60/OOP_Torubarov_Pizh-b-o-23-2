# Задание для самостоятельного решения

## Класс "Автобус" (Bus)

Экземпляру класса при инициализации передается аргумент список свойств автобуса: speed (скорость), capacity (максимальное колличество пассажиров), max_speed (максимальная скорость), passengers (список с именами пассажиров, которые уже есть в автобусе).
Класс реализует методы:
\- boarding(*passengers) - вход пассажиров в авотбус;
\- getting(*passengers) - выход пассажиров из автобуса;
\- change_speed(new_speed) - изменение скорости автобуса;
\- get_speed() - получение текущей скорости автобуса;
\- get_capacity() - получение колличества мест в автобусе;
\- get_max_speed() - получение максимальной скорости автобуса;
\- get_passengers() - получение списка имён пассажиров;
\- get_has_empty_seats() - получение информации о том, есть ли свободные места;
\- get_seats() - получение словаря с местами автобуса, где каждому месту соотвествует имя пассажира.

```PYTHON
#main.py
class Bus_Prototype:
    """
    Класс Bus_Prototype представляет прототип автобуса с определенными местами.
    """

    _seats: dict = {}

    for i in range(1, 10):
        _seats[f"seat_{i}"] = None

    def __init__(self, speed: int, capacity: int, max_speed: int, passengers):
        """
        Инициализирует объект Bus_Prototype с заданными параметрами.

        :param speed: текущая скорость автобуса
        :param capacity: вместимость автобуса
        :param maxSpeed: максимальная скорость автобуса
        :param passengers: список пассажиров в автобусе
        """
        self._speed: int = speed
        self._capacity: int = capacity
        self._max_speed: int = max_speed
        self._passengers = passengers


class Bus(Bus_Prototype):
    """
    Класс Bus представляет автобус с определенной скоростью,
    вместимостью, максимальной скоростью, пассажирами и местами.
    """

    _numb_of_seat: int = 1

    def __init__(self, speed: int, capacity: int, maxSpeed: int, passengers):
        """
        При инициализации определяет, есть ли еще свободные места в автобусе,
        и заполняет словарь с местами.
        """
        super().__init__(speed, capacity, maxSpeed, passengers)

        self._hasEmptySeats: bool

        if len(self._passengers) < self._capacity:
            self._hasEmptySeats = True
        else:
            self._hasEmptySeats = False

        for i in passengers:
            self._seats[f"seat_{self._numb_of_seat}"] = i
            self._numb_of_seat += 1

    def boarding(self, *passengers):
        """
        Метод boarding добавляет пассажиров в автобус.

        :param passengers: список пассажиров, которые хотят сесть в автобус
        """
        new_pass = list(passengers)

        for i in new_pass:
            if self._hasEmptySeats:
                if len(self._passengers) < self._capacity:
                    self._passengers.append(i)

                    for key in self._seats:
                        if self._seats[key] is None:
                            self._seats[key] = i
                            break

                    print(f"Зашёл пассажир {i}.")

                else:
                    self._hasEmptySeats = False
                    print("Свободных мест не осталось.")
            else:
                break

    def getting(self, *passengers):
        """
        Метод getting позволяет пассажирам покинуть автобус.

        :param passengers: список пассажиров, которые хотят покинуть автобус
        """
        leaving_pass = list(passengers)

        for i in leaving_pass:
            if i in self._passengers:
                self._passengers.remove(i)

                for key in self._seats:
                    if self._seats[key] == i:
                        self._seats[key] = None
                        break

                print(f"Вышел пассажир {i}")
            else:
                print(f'Пассажира "{i}" нет в автобусе.')

    def change_speed(self, new_speed: int):
        """
        Метод change_speed изменяет скорость автобуса.

        :param new_speed: новая скорость автобуса
        """
        if new_speed <= self._max_speed:
            self._speed = new_speed

    def get_speed(self):
        return self._speed

    def get_capacity(self):
        return self._capacity

    def get_max_speed(self):
        return self._max_speed

    def get_passengers(self):
        return self._passengers

    def get_has_empty_seats(self):
        return self._hasEmptySeats

    def get_seats(self):
        return self._seats 
```

``` PYTHON
#main_test.py
from main import Bus


def test_bus_initialization():
    bus = Bus(10, 20, 30, ["passenger1", "passenger2"])
    assert bus.get_speed() == 10
    assert bus.get_capacity() == 20
    assert bus.get_max_speed() == 30
    assert bus.get_passengers() == ["passenger1", "passenger2"]
    assert bus.get_has_empty_seats() is True


def test_boarding():
    bus = Bus(10, 20, 30, ["passenger1", "passenger2"])
    bus.boarding("passenger3")
    assert bus.get_passengers() == ["passenger1", "passenger2", "passenger3"]
    assert bus.get_seats()["seat_3"] == "passenger3"


def test_getting():
    bus = Bus(10, 20, 30, ["passenger1", "passenger2"])
    bus.getting("passenger1")
    assert bus.get_passengers() == ["passenger2"]
    assert bus.get_seats()["seat_1"] is None


def test_change_speed():
    bus = Bus(10, 20, 30, ["passenger1", "passenger2"])
    bus.change_speed(25)
    assert bus.get_speed() == 25

```
При выполнении задания необходимо пострить UML-диграмма классов приложения.
<p align="center"> <image src="image.png"> </p>