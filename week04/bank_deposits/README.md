# Банковские вклады
## Банк предлагает ряд вкладов для физических лиц:
* Срочный вклад: расчет прибыли осуществляется по формуле простых процентов;
* Бонусный вклад: бонус начисляется в конце периода как % от прибыли, если вклад больше определённой суммы;
* Вклад с капитализацией процентов.

Реализуйте приложение, которое бы позволило подобрать клиенту вклад по заданным параматерам.<br/>
При выполнении задания необходимо построить UML-диаграмма классов приложения

```PYTHON
#deposits.py
class Deposit:
    """
    Базовый класс для вкладов.

    Атрибуты:
        amount (float): Сумма вклада.
        period (int): Срок вклада в месяцах.
    """

    def __init__(self, amount: float, period: int) -> None:
        self.amount: float = amount
        self.period: int = period

    def calculate_profit(self):
        """
        Метод для расчета прибыли от вклада.
        """
        pass

    def get_deposit_type(self):
        """
        Метод для получения типа вклада.
        """
        pass


class ShortTermDeposit(Deposit):
    """
    Класс для срочных вкладов.

    Атрибуты:
        amount (float): Сумма вклада.
        period (int): Срок вклада в месяцах.
        rate (float): Процентная ставка.
    """

    def __init__(self, amount: float, period: int, rate: float) -> None:
        super().__init__(amount, period)
        self.rate: float = rate

    def calculate_profit(self) -> float:
        """
        Метод для расчета прибыли от срочного вклада.
        """
        return self.amount * self.rate * self.period / 100

    def get_deposit_type(self) -> str:
        """
        Метод для получения типа вклада.
        """
        return "Срочный вклад"


class BonusDeposit(Deposit):
    """
    Класс для бонусных вкладов.

    Атрибуты:
        amount (float): Сумма вклада.
        period (int): Срок вклада в месяцах.
        rate (float): Процентная ставка.
        bonus_rate (float): Бонусная процентная ставка.
        bonus_threshold (float): Порог для получения бонуса.
    """

    def __init__(
            self, amount: float, period: int, rate: float,
            bonus_rate: float, bonus_threshold: float
            ) -> None:
        super().__init__(amount, period)
        self.rate: float = rate
        self.bonus_rate: float = bonus_rate
        self.bonus_threshold: float = bonus_threshold

    def calculate_profit(self) -> float:
        """
        Метод для расчета прибыли от бонусного вклада.
        """
        profit: float = self.amount * self.rate * self.period / 100
        if profit > self.bonus_threshold:
            profit += profit * self.bonus_rate / 100
        return profit

    def get_deposit_type(self) -> str:
        """
        Метод для получения типа вклада.
        """
        return "Бонусный вклад"


class CapitalizedDeposit(Deposit):
    """
    Класс для вкладов с капитализацией процентов.

    Атрибуты:
        amount (float): Сумма вклада.
        period (int): Срок вклада в месяцах.
        rate (float): Процентная ставка.
    """

    def __init__(self, amount: float, period: int, rate: float) -> None:
        super().__init__(amount, period)
        self.rate: float = rate

    def calculate_profit(self) -> float:
        """
        Метод для расчета прибыли от вклада с капитализацией процентов.
        """
        profit: float = self.amount * (
            1 + self.rate / 100) ** self.period - self.amount
        return profit

    def get_deposit_type(self) -> str:
        """
        Метод для получения типа вклада.
        """
        return "Вклад с капитализацией процентов"

```
```PYTHON
#main.py
from deposits import *


def choose_deposit(
        amount, period, rate, bonus_rate=None, bonus_threshold=None
        ):
    if bonus_rate is not None and bonus_threshold is not None:
        return BonusDeposit(amount, period, rate, bonus_rate, bonus_threshold)
    elif bonus_rate is None and bonus_threshold is None:
        return ShortTermDeposit(amount, period, rate)
    else:
        return CapitalizedDeposit(amount, period, rate)


def main():
    print("Добро пожаловать в приложение для выбора вклада!")
    print("Введите параметры вклада:")
    amount = float(input("Сумма вклада: "))
    period = int(input("Срок вклада (в годах): "))
    rate = float(input("Процентная ставка: "))
    bonus_rate = input("Бонусная ставка (если есть): ")
    bonus_threshold = input("Порог бонуса (если есть): ")

    if bonus_rate and bonus_threshold:
        deposit = choose_deposit(
            amount, period, rate, float(bonus_rate), float(bonus_threshold)
        )
    else:
        deposit = choose_deposit(amount, period, rate)

    print("Прибыль по вкладу составит: ", deposit.calculate_profit())
    print("Тип вклада: ", deposit.get_deposit_type())


if __name__ == "__main__":
    main()

# Пример работы программы:
# Добро пожаловать в приложение для выбора вклада!
# Введите параметры вклада:
# Сумма вклада: 20000
# Срок вклада (в годах): 5
# Процентная ставка: 12
# Бонусная ставка (если есть):
# Порог бонуса (если есть):
# Прибыль по вкладу составит:  12000.0
# Тип вклада:  Срочный вклад
```