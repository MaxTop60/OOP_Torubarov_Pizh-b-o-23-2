from main import Roman


def test_roman_to_int():
    assert Roman.roman_to_int("I") == 1
    assert Roman.roman_to_int("IV") == 4
    assert Roman.roman_to_int("V") == 5
    assert Roman.roman_to_int("IX") == 9
    assert Roman.roman_to_int("X") == 10
    assert Roman.roman_to_int("XL") == 40
    assert Roman.roman_to_int("L") == 50
    assert Roman.roman_to_int("XC") == 90
    assert Roman.roman_to_int("C") == 100
    assert Roman.roman_to_int("CD") == 400
    assert Roman.roman_to_int("D") == 500
    assert Roman.roman_to_int("CM") == 900
    assert Roman.roman_to_int("M") == 1000
    assert Roman.roman_to_int("MM") == 2000
    assert Roman.roman_to_int("MMM") == 3000
    assert Roman.roman_to_int("MMMM") == 4000
    assert Roman.roman_to_int("MMMMM") == 5000
    assert Roman.roman_to_int("MMMMMM") == 6000
    assert Roman.roman_to_int("MMMMMMM") == 7000
    assert Roman.roman_to_int("MMMMMMMM") == 8000
    assert Roman.roman_to_int("MMMMMMMMM") == 9000
    assert Roman.roman_to_int("MMMMMMMMMM") == 10000


def test_int_to_roman():
    assert Roman.int_to_roman(1) == "I"
    assert Roman.int_to_roman(4) == "IV"
    assert Roman.int_to_roman(5) == "V"
    assert Roman.int_to_roman(9) == "IX"
    assert Roman.int_to_roman(10) == "X"
    assert Roman.int_to_roman(40) == "XL"
    assert Roman.int_to_roman(50) == "L"
    assert Roman.int_to_roman(90) == "XC"
    assert Roman.int_to_roman(100) == "C"
    assert Roman.int_to_roman(400) == "CD"
    assert Roman.int_to_roman(500) == "D"
    assert Roman.int_to_roman(900) == "CM"
    assert Roman.int_to_roman(1000) == "M"
    assert Roman.int_to_roman(2000) == "MM"
    assert Roman.int_to_roman(3000) == "MMM"
    assert Roman.int_to_roman(4000) == "MMMM"
    assert Roman.int_to_roman(5000) == "MMMMM"
    assert Roman.int_to_roman(6000) == "MMMMMM"
    assert Roman.int_to_roman(7000) == "MMMMMMM"
    assert Roman.int_to_roman(8000) == "MMMMMMMM"
    assert Roman.int_to_roman(9000) == "MMMMMMMMM"
    assert Roman.int_to_roman(10000) == "MMMMMMMMMM"


def test_add():
    roman1 = Roman("I")
    roman2 = Roman("V")
    assert roman1 + roman2 == "VI"


def test_sub():
    roman1 = Roman("V")
    roman2 = Roman("I")
    assert roman1 - roman2 == "IV"


def test_mul():
    roman1 = Roman("V")
    roman2 = Roman("I")
    assert roman1 * roman2 == "V"


def test_truediv():
    roman1 = Roman("V")
    roman2 = Roman("I")
    assert roman1 / roman2 == "V"
