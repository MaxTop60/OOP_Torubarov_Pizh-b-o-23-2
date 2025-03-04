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
