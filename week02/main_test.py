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
