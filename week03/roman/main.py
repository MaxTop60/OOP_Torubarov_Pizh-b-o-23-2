class Roman:
    def __init__(self, roman_number: str):
        self._roman_number: str = roman_number

    @staticmethod
    def roman_to_int(roman_number) -> int:
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
                and roman_dict[roman_number[i]] < roman_dict[
                    roman_number[i + 1]]
            ):
                result -= roman_dict[roman_number[i]]
            else:
                result += roman_dict[roman_number[i]]
        return result
    
    @staticmethod 
    def int_to_roman(number: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while i > 0:
            for el in range(i // val[i]):
                roman_num += syb[i]
                i -= val[i]
            i += 1
        return roman_num
