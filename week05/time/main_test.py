from unittest.mock import MagicMock, patch
from Time import Time
from Time_Collection import Time_Collection

# Создаем тестовые объекты Time
time1 = Time(1, 2, 3)
time2 = Time(4, 5, 6)


# Тестирование инициализации коллекции
def test_init():
    collection = Time_Collection(time1, time2)
    assert collection._data == [time1, time2]


# Тестирование метода __str__
def test_str():
    collection = Time_Collection(time1, time2)
    assert str(collection) == "Times: ['01:02:03', '04:05:06']"


# Тестирование метода __getitem__
def test_getitem():
    collection = Time_Collection(time1, time2)
    assert collection[0] == time1
    assert collection[1] == time2


# Тестирование метода add
def test_add():
    collection = Time_Collection()
    collection.add(time1)
    assert collection._data == [time1]


# Тестирование метода remove
def test_remove():
    collection = Time_Collection(time1, time2)
    collection.remove(0)
    assert collection._data == [time2]


# Тестирование метода save
@patch("builtins.open", new_callable=MagicMock)
def test_save(mock_open):
    collection = Time_Collection(time1, time2)
    collection.save("test.json")
    mock_open.assert_called_once_with("test.json", "w")


# Тестирование метода load
@patch("builtins.open", new_callable=MagicMock)
def test_load(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = '' \
    '{"Times": [{"hours": 1, "minutes": 2, "seconds": 3},' \
    ' {"hours": 4, "minutes": 5, "seconds": 6}]}'

    collection = Time_Collection.load("test.json")
    assert collection._data[0].hours == time1.hours
    assert collection._data[0].minutes == time1.minutes
    assert collection._data[0].seconds == time1.seconds
    assert collection._data[1].hours == time2.hours
    assert collection._data[1].minutes == time2.minutes
    assert collection._data[1].seconds == time2.seconds
