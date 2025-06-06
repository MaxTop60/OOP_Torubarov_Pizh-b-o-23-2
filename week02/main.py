from abc import abstractmethod, ABC


class Bus_Prototype(ABC):
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

    @abstractmethod
    def boarding(self, *passengers: str):
        pass


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

    def boarding(self, *passengers: str):
        """
        Метод boarding добавляет пассажиров в автобус.

        :param passengers: список пассажиров, которые хотят сесть в автобус
        """
        new_pass = list(passengers)

        for i in new_pass:
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
        print(self._seats)
        return self._seats

    def __str__(self):
        return (
            f"Скорость автобуса: {self._speed} км/час\n"
            f"Максимальная скорость автобуса: {self._max_speed} км/час\n"
            f"Колличество свободных мест: "
            f"{len(self._passengers) - self._capacity}\n"
            f"Колличество пассажиров: {len(self._passengers)}"
        )
