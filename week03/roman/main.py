class Roman:
    """
    Класс для работы с римскими числами.
    """

    def __init__(self, roman_number: str):
        """
        Инициализация объекта класса Roman.

        :param roman_number: римское число в виде строки
        """
        self._roman_number: str = roman_number

    @staticmethod
    def roman_to_int(roman_number) -> int:
        """
        Преобразование римского числа в целое число.

        :param roman_number: римское число в виде строки
        :return: целое число
        """
        for i in roman_number:
            if i not in "IVXLCDM":
                raise ValueError("Invalid roman number")
        roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
            }
        result = 0
        for i in range(len(roman_number)):
            if (
                i < len(roman_number) - 1
                and roman_dict[roman_number[i]] < roman_dict[roman_number[
                    i + 1]]
            ):
                result -= roman_dict[roman_number[i]]
            else:
                result += roman_dict[roman_number[i]]
        return result

    @staticmethod
    def int_to_roman(number: int) -> str:
        """
        Преобразование целого числа в римское число.

        :param number: целое число
        :return: римское число в виде строки
        """
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L",
               "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ""
        i = 0
        while number > 0:
            for el in range(int(number // val[i])):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num

    def __add__(self, other):
        """
        Сложение двух римских чисел.

        :param other: объект класса Roman
        :return: результат сложения в виде римского числа
        """
        return Roman.int_to_roman(
            self.roman_to_int(self._roman_number)
            + self.roman_to_int(other._roman_number)
        )

    def __sub__(self, other):
        """
        Вычитание двух римских чисел.

        :param other: объект класса Roman
        :return: результат вычитания в виде римского числа
        """
        return Roman.int_to_roman(
            self.roman_to_int(self._roman_number)
            - self.roman_to_int(other._roman_number)
        )

    def __mul__(self, other):
        """
        Умножение двух римских чисел.

        :param other: объект класса Roman
        :return: результат умножения в виде римского числа
        """
        return Roman.int_to_roman(
            self.roman_to_int(self._roman_number)
            * self.roman_to_int(other._roman_number)
        )

    def __truediv__(self, other):
        """
        Деление двух римских чисел.

        :param other: объект класса Roman
        :return: результат деления в виде римского числа
        """
        return Roman.int_to_roman(
            self.roman_to_int(self._roman_number)
            / self.roman_to_int(other._roman_number)
        )
