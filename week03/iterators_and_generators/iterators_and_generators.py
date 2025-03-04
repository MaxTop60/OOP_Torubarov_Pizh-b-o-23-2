numbers_1 = [1, 3, 4, 6, 9, 11]
numbers_2 = [1, 4, 11]


def calculate_squares(numbers: list):
    """
    Функция принимает список чисел и возвращает генератор,
    который вычисляет квадраты чисел, кратных 3.

    Args:
        numbers (list): Список чисел.

    Returns:
        generator: Генератор, вычисляющий квадраты чисел, кратных 3.
    """
    return (x**2 for x in numbers if x % 3 == 0)


squares_1 = calculate_squares(numbers_1)
squares_2 = calculate_squares(numbers_2)

print(sum(squares_1))
# Выведется: 126
print(sum(squares_2))
# Выведется: 0
