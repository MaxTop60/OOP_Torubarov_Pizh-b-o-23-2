from main import Bus


def test_boarding():
    bus = Bus(60, 10, 120, [])
    bus.boarding("passenger1", "passenger2")
    assert bus.get_passengers() == ["passenger1", "passenger2"]
    assert bus.get_seats() == {
        "seat_1": "passenger1",
        "seat_2": "passenger2",
        "seat_3": None,
        "seat_4": None,
        "seat_5": None,
        "seat_6": None,
        "seat_7": None,
        "seat_8": None,
        "seat_9": None,
    }


def test_getting():
    bus = Bus(60, 10, 120, ["passenger1", "passenger2"])
    bus.getting("passenger1")
    assert bus.get_passengers() == ["passenger2"]
    assert bus.get_seats() == {
        "seat_1": None,
        "seat_2": "passenger2",
        "seat_3": None,
        "seat_4": None,
        "seat_5": None,
        "seat_6": None,
        "seat_7": None,
        "seat_8": None,
        "seat_9": None,
    }


def test_change_speed():
    bus = Bus(60, 10, 120, [])
    bus.change_speed(80)
    assert bus.get_speed() == 80


def test_get_speed():
    bus = Bus(60, 10, 120, [])
    assert bus.get_speed() == 60


def test_get_capacity():
    bus = Bus(60, 10, 120, [])
    assert bus.get_capacity() == 10


def test_get_max_speed():
    bus = Bus(60, 10, 120, [])
    assert bus.get_max_speed() == 120


def test_get_passengers():
    bus = Bus(60, 10, 120, ["passenger1", "passenger2"])
    assert bus.get_passengers() == ["passenger1", "passenger2"]


def test_get_has_empty_seats():
    bus = Bus(60, 10, 120, ["passenger1", "passenger2"])
    assert bus.get_has_empty_seats() is True


def test_get_seats():
    bus = Bus(60, 10, 120, ["passenger1", "passenger2"])
    assert bus.get_seats() == {
        "seat_1": "passenger1",
        "seat_2": "passenger2",
        "seat_3": None,
        "seat_4": None,
        "seat_5": None,
        "seat_6": None,
        "seat_7": None,
        "seat_8": None,
        "seat_9": None,
    }


def test_str():
    bus = Bus(60, 10, 120, ["passenger1", "passenger2"])
    print(bus)
