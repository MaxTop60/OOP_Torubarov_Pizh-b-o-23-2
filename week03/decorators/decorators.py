def format_float_return(func):
    """
    Декоратор, который округляет результат функции до двух знаков
    после запятой, если результат является числом с плавающей точкой.
    """

    def wrapper():
        result = func()
        if type(result) is float:
            return round(result, 2)
        else:
            return result

    return wrapper


@format_float_return
def func1():
    """
    Функция, которая возвращает число с плавающей точкой.
    """
    return 1.123456789


@format_float_return
def func2():
    """
    Функция, которая возвращает целое число.
    """
    return 1


@format_float_return
def func3():
    """
    Функция, которая возвращает строку.
    """
    return "Привет"


print(func1())
# 1.12
print(func2())
# 1
print(func3())
# Привет
