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